import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def smape(y_true, y_pred):
    denominator = (np.abs(y_true) + np.abs(y_pred)) / 200.0
    diff = np.abs(y_true - y_pred) / denominator
    diff[denominator == 0] = 0.0
    return np.nanmean(diff)


n_rows = 10
n_columns = 10


def main():
    data = pd.DataFrame.from_csv('train_1.csv')
    time_x = data.columns.values
    time_x = np.array(list(map(lambda day_str: datetime.datetime.strptime(day_str, '%Y-%m-%d'), time_x)))

    plt.figure(1, figsize=(10, 10))
    for i in range(n_columns*n_rows):
        plt.subplot(n_columns, n_rows, i+1)
        plt.plot(time_x, data.values[i, :])
    plt.show()


main()

