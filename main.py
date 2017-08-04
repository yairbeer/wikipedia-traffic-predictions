import numpy as np

from keyHandler import KeyHandler
from dataHandler import DataHandler
from submissionHandler import SubmissionHandler
from constants import START_DATE_1, END_DATE_1

np.seterr(divide='ignore', invalid='ignore')


def main():
    print('start')

    """CV"""
    # print('Start CV')
    # data_handler = DataHandler('train_1.csv')
    # data_handler.generate_evaluation(90)
    # for train_days in range(10, 110, 10):
    #     print(train_days, ' days')
    #     data_handler.predict_site_median(train_days, replace_nan=0)
    #     print('Median: SMAPE ', data_handler.smape(data_handler.evaluation_y.values, data_handler.test.values))
    #     data_handler.predict_site_best_smape(10, train_days)
    #     print('Best SMAPE: SMAPE ', data_handler.smape(data_handler.evaluation_y, data_handler.test))
    """
    Median is the best for the last 10 days for the range(10, 60, 10)
    """

    """Submission"""

    data_handler = DataHandler('train_1.csv')
    data_handler.generate_test(START_DATE_1, END_DATE_1)
    key_handler = KeyHandler('key_1.csv')
    submission_handler = SubmissionHandler('sample_submission_1.csv', key_handler)

    data_handler.predict_site_median(days_train=50)
    submission_handler.save_prediction(data_handler.test, 'predictions_1/median_50_days_nans_to_300.csv', fillna=300)

    print('completed successfully')

main()
