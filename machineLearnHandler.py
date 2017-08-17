import pandas as pd
import numpy as np
import datetime

from constants import DATE_FORMAT


class MachineLearningHandler:
    def __init__(self, train_filename):
        print('reading train')
        self.train = pd.DataFrame.from_csv(train_filename)
        self.test = None
        self.evaluation_y = None

    def generate_row_features(self):
        row_names = self.train.values
        parsed_rows = np.zeros((row_names.size, 3)).astype(str)
        for i in np.arange(row_names.size):
            split_row = row_names[i].split('_')
            if len(split_row) == 4:
                parsed_rows[i, :] = split_row
            else:
                parsed_rows[i, :] = split_row[-3:]
        parsed_rows = pd.DataFrame(
            parsed_rows[:, 1:], columns=['project', 'access', 'agent'], index=self.train.index.values)
        parsed_rows = pd.get_dummies(parsed_rows)
        return parsed_rows

    def generate_evaluation(self, days):
        self.evaluation_y = self.train.iloc[:, -1*days:]
        self.train = self.train.iloc[:, :-1*days]
        self.generate_test(self.evaluation_y.columns.values[0], self.evaluation_y.columns.values[-1])

    def predict_site_mean(self, days_train=None, replace_nan=None):
        print('predicting median')
        train = self.train.values[:, -days_train:] if days_train else self.train.values
        prediction_array = np.nanmean(train).astype(int)
        prediction_array[np.isnan(prediction_array)] = replace_nan
        prediction_array = np.repeat(prediction_array.reshape((-1, 1)), self.test.shape[1], axis=1)
        self.test.iloc[:, :] = prediction_array

    def predict_site_median(self, days_train=None, replace_nan=None):
        print('predicting median')
        train = self.train.values[:, -days_train:] if days_train else self.train.values
        prediction_array = np.nanmedian(train).astype(int)
        prediction_array[np.isnan(prediction_array)] = replace_nan
        prediction_array = np.repeat(prediction_array.reshape((-1, 1)), self.test.shape[1], axis=1)
        self.test.iloc[:, :] = prediction_array

    def generate_test(self, start_date, end_date):
        self.test = pd.DataFrame(
            data=0, index=self.train.index, columns=self._generate_dates_columns(start_date, end_date))

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
