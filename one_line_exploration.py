import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from pandas.compat import lmap

from sklearn.linear_model import LinearRegression


def autocorrelation_plot(series, n_samples=None, ax=None, **kwds):
    """Autocorrelation plot for time series.

    Parameters:
    -----------
    series: Time series
    ax: Matplotlib axis object, optional
    kwds : keywords
        Options to pass to matplotlib plotting method

    Returns:
    -----------
    ax: Matplotlib axis object
    """
    import matplotlib.pyplot as plt
    n = len(series)
    data = np.asarray(series)
    if ax is None:
        ax = plt.gca(xlim=(1, n_samples), ylim=(-1.0, 1.0))
    mean = np.mean(data)
    c0 = np.sum((data - mean) ** 2) / float(n)

    def r(h):
        return ((data[:n - h] - mean) *
                (data[h:] - mean)).sum() / float(n) / c0
    x = (np.arange(n) + 1).astype(int)
    y = lmap(r, x)
    z95 = 1.959963984540054
    z99 = 2.5758293035489004
    ax.axhline(y=z99 / np.sqrt(n), linestyle='--', color='grey')
    ax.axhline(y=z95 / np.sqrt(n), color='grey')
    ax.axhline(y=0.0, color='black')
    ax.axhline(y=-z95 / np.sqrt(n), color='grey')
    ax.axhline(y=-z99 / np.sqrt(n), linestyle='--', color='grey')
    ax.set_xlabel("Lag")
    ax.set_ylabel("Autocorrelation")
    if n_samples:
        ax.plot(x[:n_samples], y[:n_samples], **kwds)
    else:
        ax.plot(x, y, **kwds)
    if 'label' in kwds:
        ax.legend()
    ax.grid()
    return ax


def smape(y_true, y_pred):
    denominator = (np.abs(y_true) + np.abs(y_pred)) / 200.0
    diff = np.abs(y_true - y_pred) / denominator
    diff[denominator == 0] = 0.0
    return np.nanmean(diff)


def main():
    train_dates = ["2015-07-01","2015-07-02","2015-07-03","2015-07-04","2015-07-05","2015-07-06","2015-07-07","2015-07-08","2015-07-09","2015-07-10","2015-07-11","2015-07-12","2015-07-13","2015-07-14","2015-07-15","2015-07-16","2015-07-17","2015-07-18","2015-07-19","2015-07-20","2015-07-21","2015-07-22","2015-07-23","2015-07-24","2015-07-25","2015-07-26","2015-07-27","2015-07-28","2015-07-29","2015-07-30","2015-07-31","2015-08-01","2015-08-02","2015-08-03","2015-08-04","2015-08-05","2015-08-06","2015-08-07","2015-08-08","2015-08-09","2015-08-10","2015-08-11","2015-08-12","2015-08-13","2015-08-14","2015-08-15","2015-08-16","2015-08-17","2015-08-18","2015-08-19","2015-08-20","2015-08-21","2015-08-22","2015-08-23","2015-08-24","2015-08-25","2015-08-26","2015-08-27","2015-08-28","2015-08-29","2015-08-30","2015-08-31","2015-09-01","2015-09-02","2015-09-03","2015-09-04","2015-09-05","2015-09-06","2015-09-07","2015-09-08","2015-09-09","2015-09-10","2015-09-11","2015-09-12","2015-09-13","2015-09-14","2015-09-15","2015-09-16","2015-09-17","2015-09-18","2015-09-19","2015-09-20","2015-09-21","2015-09-22","2015-09-23","2015-09-24","2015-09-25","2015-09-26","2015-09-27","2015-09-28","2015-09-29","2015-09-30","2015-10-01","2015-10-02","2015-10-03","2015-10-04","2015-10-05","2015-10-06","2015-10-07","2015-10-08","2015-10-09","2015-10-10","2015-10-11","2015-10-12","2015-10-13","2015-10-14","2015-10-15","2015-10-16","2015-10-17","2015-10-18","2015-10-19","2015-10-20","2015-10-21","2015-10-22","2015-10-23","2015-10-24","2015-10-25","2015-10-26","2015-10-27","2015-10-28","2015-10-29","2015-10-30","2015-10-31","2015-11-01","2015-11-02","2015-11-03","2015-11-04","2015-11-05","2015-11-06","2015-11-07","2015-11-08","2015-11-09","2015-11-10","2015-11-11","2015-11-12","2015-11-13","2015-11-14","2015-11-15","2015-11-16","2015-11-17","2015-11-18","2015-11-19","2015-11-20","2015-11-21","2015-11-22","2015-11-23","2015-11-24","2015-11-25","2015-11-26","2015-11-27","2015-11-28","2015-11-29","2015-11-30","2015-12-01","2015-12-02","2015-12-03","2015-12-04","2015-12-05","2015-12-06","2015-12-07","2015-12-08","2015-12-09","2015-12-10","2015-12-11","2015-12-12","2015-12-13","2015-12-14","2015-12-15","2015-12-16","2015-12-17","2015-12-18","2015-12-19","2015-12-20","2015-12-21","2015-12-22","2015-12-23","2015-12-24","2015-12-25","2015-12-26","2015-12-27","2015-12-28","2015-12-29","2015-12-30","2015-12-31","2016-01-01","2016-01-02","2016-01-03","2016-01-04","2016-01-05","2016-01-06","2016-01-07","2016-01-08","2016-01-09","2016-01-10","2016-01-11","2016-01-12","2016-01-13","2016-01-14","2016-01-15","2016-01-16","2016-01-17","2016-01-18","2016-01-19","2016-01-20","2016-01-21","2016-01-22","2016-01-23","2016-01-24","2016-01-25","2016-01-26","2016-01-27","2016-01-28","2016-01-29","2016-01-30","2016-01-31","2016-02-01","2016-02-02","2016-02-03","2016-02-04","2016-02-05","2016-02-06","2016-02-07","2016-02-08","2016-02-09","2016-02-10","2016-02-11","2016-02-12","2016-02-13","2016-02-14","2016-02-15","2016-02-16","2016-02-17","2016-02-18","2016-02-19","2016-02-20","2016-02-21","2016-02-22","2016-02-23","2016-02-24","2016-02-25","2016-02-26","2016-02-27","2016-02-28","2016-02-29","2016-03-01","2016-03-02","2016-03-03","2016-03-04","2016-03-05","2016-03-06","2016-03-07","2016-03-08","2016-03-09","2016-03-10","2016-03-11","2016-03-12","2016-03-13","2016-03-14","2016-03-15","2016-03-16","2016-03-17","2016-03-18","2016-03-19","2016-03-20","2016-03-21","2016-03-22","2016-03-23","2016-03-24","2016-03-25","2016-03-26","2016-03-27","2016-03-28","2016-03-29","2016-03-30","2016-03-31","2016-04-01","2016-04-02","2016-04-03","2016-04-04","2016-04-05","2016-04-06","2016-04-07","2016-04-08","2016-04-09","2016-04-10","2016-04-11","2016-04-12","2016-04-13","2016-04-14","2016-04-15","2016-04-16","2016-04-17","2016-04-18","2016-04-19","2016-04-20","2016-04-21","2016-04-22","2016-04-23","2016-04-24","2016-04-25","2016-04-26","2016-04-27","2016-04-28","2016-04-29","2016-04-30","2016-05-01","2016-05-02","2016-05-03","2016-05-04","2016-05-05","2016-05-06","2016-05-07","2016-05-08","2016-05-09","2016-05-10","2016-05-11","2016-05-12","2016-05-13","2016-05-14","2016-05-15","2016-05-16","2016-05-17","2016-05-18","2016-05-19","2016-05-20","2016-05-21","2016-05-22","2016-05-23","2016-05-24","2016-05-25","2016-05-26","2016-05-27","2016-05-28","2016-05-29","2016-05-30","2016-05-31","2016-06-01","2016-06-02","2016-06-03","2016-06-04","2016-06-05","2016-06-06","2016-06-07","2016-06-08","2016-06-09","2016-06-10","2016-06-11","2016-06-12","2016-06-13","2016-06-14","2016-06-15","2016-06-16","2016-06-17","2016-06-18","2016-06-19","2016-06-20","2016-06-21","2016-06-22","2016-06-23","2016-06-24","2016-06-25","2016-06-26","2016-06-27","2016-06-28","2016-06-29","2016-06-30","2016-07-01","2016-07-02","2016-07-03","2016-07-04","2016-07-05","2016-07-06","2016-07-07","2016-07-08","2016-07-09","2016-07-10","2016-07-11","2016-07-12","2016-07-13","2016-07-14","2016-07-15","2016-07-16","2016-07-17","2016-07-18","2016-07-19","2016-07-20","2016-07-21","2016-07-22","2016-07-23","2016-07-24","2016-07-25","2016-07-26","2016-07-27","2016-07-28","2016-07-29","2016-07-30","2016-07-31","2016-08-01","2016-08-02","2016-08-03","2016-08-04","2016-08-05","2016-08-06","2016-08-07","2016-08-08","2016-08-09","2016-08-10","2016-08-11","2016-08-12","2016-08-13","2016-08-14","2016-08-15","2016-08-16","2016-08-17","2016-08-18","2016-08-19","2016-08-20","2016-08-21","2016-08-22","2016-08-23","2016-08-24","2016-08-25","2016-08-26","2016-08-27","2016-08-28","2016-08-29","2016-08-30","2016-08-31","2016-09-01","2016-09-02","2016-09-03","2016-09-04","2016-09-05","2016-09-06","2016-09-07","2016-09-08","2016-09-09","2016-09-10","2016-09-11","2016-09-12","2016-09-13","2016-09-14","2016-09-15","2016-09-16","2016-09-17","2016-09-18","2016-09-19","2016-09-20","2016-09-21","2016-09-22","2016-09-23","2016-09-24","2016-09-25","2016-09-26","2016-09-27","2016-09-28","2016-09-29","2016-09-30","2016-10-01","2016-10-02","2016-10-03","2016-10-04","2016-10-05","2016-10-06","2016-10-07","2016-10-08","2016-10-09","2016-10-10","2016-10-11","2016-10-12","2016-10-13","2016-10-14","2016-10-15","2016-10-16","2016-10-17","2016-10-18","2016-10-19","2016-10-20","2016-10-21","2016-10-22","2016-10-23","2016-10-24","2016-10-25","2016-10-26","2016-10-27","2016-10-28","2016-10-29","2016-10-30","2016-10-31","2016-11-01","2016-11-02","2016-11-03","2016-11-04","2016-11-05","2016-11-06","2016-11-07","2016-11-08","2016-11-09","2016-11-10","2016-11-11","2016-11-12","2016-11-13","2016-11-14","2016-11-15","2016-11-16","2016-11-17","2016-11-18","2016-11-19","2016-11-20","2016-11-21","2016-11-22","2016-11-23","2016-11-24","2016-11-25","2016-11-26","2016-11-27","2016-11-28","2016-11-29","2016-11-30","2016-12-01","2016-12-02","2016-12-03","2016-12-04","2016-12-05","2016-12-06","2016-12-07","2016-12-08","2016-12-09","2016-12-10","2016-12-11","2016-12-12","2016-12-13","2016-12-14","2016-12-15","2016-12-16","2016-12-17","2016-12-18","2016-12-19","2016-12-20","2016-12-21","2016-12-22","2016-12-23","2016-12-24","2016-12-25","2016-12-26","2016-12-27","2016-12-28","2016-12-29","2016-12-30","2016-12-31"]
    train_y = [18,11,5,13,14,9,9,22,26,24,19,10,14,15,8,16,8,8,16,7,11,10,20,18,15,14,49,10,16,18,8,5,9,7,13,9,7,4,11,10,5,9,9,9,9,13,4,15,25,9,5,6,20,3,14,46,5,5,13,4,9,10,9,11,11,11,9,15,5,10,7,4,8,9,10,6,13,16,6,24,9,11,12,8,14,6,6,11,14,6,10,20,7,15,8,15,5,8,8,5,11,165,34,6,13,8,9,11,26,18,3,5,12,6,16,19,9,10,11,11,7,9,10,24,6,6,8,16,13,10,10,6,5,20,6,47,9,9,12,11,17,15,14,11,97,11,12,11,14,15,12,104,5,22,45,75,29,34,20,12,25,9,62,20,19,8,23,13,16,34,36,11,18,12,24,30,27,44,35,53,11,26,13,18,9,16,6,19,20,19,22,30,14,16,22,15,15,26,16,13,27,18,13,32,31,16,38,18,9,14,10,24,8,15,18,10,23,17,11,26,14,8,12,9,11,34,17,29,11,9,14,21,12,11,13,11,13,16,13,19,21,14,11,35,18,42,15,5,21,56,9,20,17,18,8,9,17,9,10,14,17,6,18,13,11,12,11,8,15,11,20,59,11,18,17,12,14,13,9,490,189,102,38,126,71,21,57,79,17,17,23,16,23,18,22,44,6,31,17,25,40,19,15,15,29,18,16,13,20,22,19,11,50,22,39,23,21,23,22,16,19,35,16,12,15,13,14,10,21,20,19,14,12,15,17,16,21,27,13,11,15,14,18,18,10,11,14,18,14,13,17,15,14,234,8,62,26,22,8,22,15,69,11,18,23,12,20,17,15,16,18,21,15,30,115,56,45,17,18,15,18,14,15,15,24,22,18,30,12,13,18,17,31,26,29,12,19,19,57,17,20,49,10,19,26,41,23,30,55,17,24,14,12,49,42,37,13,30,20,33,20,14,40,15,18,26,8,25,21,20,25,19,23,18,19,18,55,16,65,11,11,13,20,21,13,24,20,13,32,16,10,13,44,17,13,72,40,19,14,13,12,14,10,26,13,22,14,23,12,8,50,13,10,16,14,10,24,10,20,10,26,25,16,19,20,12,19,50,16,30,18,25,14,20,8,67,13,41,10,21,13,8,15,14,12,6,11,10,42,21,24,14,11,204,14,45,33,28,18,14,47,15,14,18,20,14,16,14,20,60,22,15,17,19,18,21,21,47,65,17,32,63,15,26,14,20,22,19,18,20]
    train_y = np.array(train_y)
    train_eval_n = 100
    train_n = len(train_y) - train_eval_n
    print(len(train_dates), len(train_y))

    train_day_of_week = []
    train_lm_x = []
    for i in range(len(train_y)):
        train_dates[i] = datetime.datetime.strptime(train_dates[i], "%Y-%m-%d")
        train_day_of_week.append(train_dates[i].weekday())
        train_lm_x.append((train_dates[i] - datetime.datetime(2015,7,1)).total_seconds()/(24*3600))

    mean_result = np.mean(train_y[:train_n])
    median_result = np.median(train_y[:train_n])

    # Linear prediciton
    train_lm_x = np.array([train_lm_x]).reshape((-1, 1))
    lm_date = LinearRegression()
    lm_date.fit(train_lm_x[:train_n], train_y[:train_n])
    print(lm_date.coef_, lm_date.intercept_, lm_date.residues_)
    linear_date_prediction = lm_date.predict(train_lm_x[train_n:])

    plt.plot(train_dates, train_y, 'r',
             train_dates[train_n:], linear_date_prediction, 'b--')
    plt.show()

    # # Days of the week
    # train_day_of_week = pd.Series(train_day_of_week)
    # train_day_of_week = pd.get_dummies(train_day_of_week)
    #
    # lm_day_of_week = LinearRegression(fit_intercept=False)
    # lm_day_of_week.fit(train_day_of_week.values, train_y)
    # linear_weekday_prediction = lm_day_of_week.predict(train_day_of_week.values)
    # print(lm_day_of_week.coef_, lm_day_of_week.intercept_, lm_day_of_week.residues_)

    data_series = pd.Series(train_y)
    autocorrelation_plot(data_series, n_samples=20)
    plt.show()
    #
    # plt.plot(train_dates, train_y)
    # plt.show()

    print('SMAPE results')
    print('Mean ', smape(train_y, mean_result))
    print('Median ', smape(train_y, median_result))
    print('Linear regression (days) ', smape(train_y[train_n:], linear_date_prediction))
    # print('Linear regression (weekday) ', smape(train_y, linear_weekday_prediction + linear_date_prediction))

main()

