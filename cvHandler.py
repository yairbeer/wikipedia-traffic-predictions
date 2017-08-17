import pandas as pd
import numpy as np
import datetime

from constants import DATE_FORMAT


class CVHandler:
    def __init__(self, train_filename, n_cv, train_periods, test_periods):
        print('reading train')
        self.train = pd.DataFrame.from_csv(train_filename)
        self.cv_column_indices = None
        self.generate_cv_columns_indices(n_cv, train_periods, test_periods)

    def generate_cv_columns_indices(self, n, n_train_periods, n_test_periods):
        columns = self.train.columns.values
        cv_indices = []
        for i in range(columns.size, -1+n_train_periods+n_test_periods, -n_test_periods):
            test_indices = range(i-n_test_periods, i)
            train_indices = range(i-n_test_periods-n_train_periods, i-n_test_periods)
            cv_indices.append((train_indices, test_indices))
        if len(cv_indices) >= n:
            self.cv_column_indices = cv_indices[-n:]
        else:
            print('There are only %d periods' % len(cv_indices))
            self.cv_column_indices = cv_indices[-n:]

    @staticmethod
    def predict_from_1d(arr, n_test_columns, replace_nan=None):
        arr[np.isnan(arr)] = replace_nan
        arr = np.repeat(arr.reshape((-1, 1)), n_test_columns, axis=1)
        return arr

    def predict_site_mean(self, train, n_train, replace_nan=None):
        print('predicting mean')
        train = train.iloc[:, -n_train:]
        prediction_array = np.nanmean(train, axis=1)
        prediction_array[np.isnan(prediction_array)] = replace_nan
        return prediction_array

    def predict_site_median(self, train, n_train, replace_nan=None):
        print('predicting median')
        train = train.iloc[:, -n_train:]
        prediction_array = np.nanmedian(train, axis=1)
        prediction_array[np.isnan(prediction_array)] = replace_nan
        return prediction_array

    def predict_site_log_mean(self, train, n_train, replace_nan=None):
        print('predicting log mean')
        train = train.iloc[:, -n_train:]
        train = np.log(1+train)
        prediction_array = np.nanmean(train, axis=1)
        prediction_array[np.isnan(prediction_array)] = replace_nan
        prediction_array = np.exp(prediction_array) - 1
        return prediction_array

    def calculate_momentum(self, arr, alpha, trend):
        print('calculating momentum')
        last_count = arr[:, 1]
        count_nans = np.isnan(last_count)
        last_count[count_nans] = arr[count_nans, 0]

        medians = np.nanmedian(arr, axis=1)
        count_nans = np.isnan(last_count)
        last_count[count_nans] = medians[count_nans]

        last_momentum = arr[:, 1] - arr[:, 0]
        count_nans = np.isnan(last_momentum)
        last_momentum[count_nans] = 0

        count = last_count
        momentum = last_momentum

        for i in range(2, arr.shape[1]):
            count = alpha * arr[:, i] + (1 - alpha) * (last_count + last_momentum)
            count_nans = np.isnan(arr[:, i])
            count[count_nans] = last_count[count_nans]

            momentum = trend * (count - last_count) + (1 - trend) * last_momentum
            count_nans = np.isnan(arr[:, i])
            momentum[count_nans] = last_momentum[count_nans]

            last_count = count
            last_momentum = momentum

        return count, momentum

    def replace_nan(self, value=0):
        print('replacing train NaNs to ' + str(value))
        self.train = pd.DataFrame.fillna(self.train, value=value)

    @staticmethod
    def _generate_dates_columns(start_date, end_date):
        dates = []
        current_date = datetime.datetime.strptime(start_date, DATE_FORMAT)
        end_date = datetime.datetime.strptime(end_date, DATE_FORMAT)
        while current_date <= end_date:
            dates.append(current_date.strftime(DATE_FORMAT))
            current_date = current_date + datetime.timedelta(days=1)
        return dates

    @staticmethod
    def smape(y_true, y_pred):
        denominator = (np.abs(y_true) + np.abs(y_pred)) / 200.0
        diff = np.abs(y_true - y_pred) / denominator
        diff[denominator == 0] = 0
        return np.nanmean(diff)
