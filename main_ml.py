import numpy as np

from keyHandler import KeyHandler
from machineLearnHandler import MachineLearningHandler
from submissionHandler import SubmissionHandler
from constants import START_DATE_1, END_DATE_1

np.seterr(divide='ignore', invalid='ignore')


def main():
    print('start')

    """CV"""
    print('Start CV')
    ml_handler = MachineLearningHandler('train_1.csv')
    ml_handler.generate_evaluation(90)
    
    ml_handler.generate_row_features()
    for train_days in range(10, 110, 10):
        print(train_days, ' days')
        ml_handler.predict_site_median(train_days, replace_nan=0)
        print('Median: SMAPE ', ml_handler.smape(ml_handler.evaluation_y.values, ml_handler.test.values))

    """
    Median is the best for the last 10 days for the range(10, 60, 10)
    """

    """Submission"""

    # ml_handler = DataHandler('train_1.csv')
    # ml_handler.generate_test(START_DATE_1, END_DATE_1)
    # key_handler = KeyHandler('key_1.csv')
    # submission_handler = SubmissionHandler('sample_submission_1.csv', key_handler)
    #
    # ml_handler.predict_site_median(days_train=50, replace_nan=300)
    # submission_handler.save_prediction(ml_handler.test, 'predictions_1/median_50_days_nans_to_300.csv')

    print('completed successfully')

main()
