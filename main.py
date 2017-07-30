from keyHandler import KeyHandler
from dataHandler import DataHandler
from submissionHandler import SubmissionHandler
from constants import START_DATE_1, END_DATE_1


def main():
    print('start')
    key_handler = KeyHandler('key_1.csv')
    data_handler = DataHandler('train_1.csv')
    submission_handler = SubmissionHandler('sample_submission_1.csv', key_handler)

    # data_handler.predict_site_mean(START_DATE_1, END_DATE_1)
    # submission_handler.save_prediction(data_handler.test1, 'predictions_1/mean_benchmark_no_nans.csv')
    #
    # data_handler.predict_site_median(START_DATE_1, END_DATE_1)
    # submission_handler.save_prediction(data_handler.test1, 'predictions_1/median_benchmark_no_nans.csv')
    #
    # data_handler.predict_site_best_smape(START_DATE_1, END_DATE_1, 50)
    # submission_handler.save_prediction(data_handler.test1, 'predictions_1/train_best_smape_n=50_no_nans.csv')
    #
    # data_handler.predict_site_median(START_DATE_1, END_DATE_1, days_train=50)
    # submission_handler.save_prediction(data_handler.test1, 'predictions_1/median_50_days_no_nans.csv')

    data_handler.predict_site_best_smape(START_DATE_1, END_DATE_1, 50, days_train=50)
    submission_handler.save_prediction(data_handler.test1, 'predictions_1/smape_50_days_no_nans.csv')

    print('completed successfully')

main()
