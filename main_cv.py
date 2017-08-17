import numpy as np
from cvHandler import CVHandler

np.seterr(divide='ignore', invalid='ignore')


def main():
    print('Start CV')
    cv_handler = CVHandler('train_1.csv', 5, 90, 90)
    results = []
    train_days = 30
    for i in range(10, 20, 10):
        print('For train days %s' % train_days)

        for train_indices, test_indices in cv_handler.cv_column_indices:
            # cv_handler.calculate_momentum(cv_handler.train.iloc[:, train_indices], alpha, 0)
            current_median_scores = []
            current_mean_scores = []
            current_log_mean_scores = []

            prediction = cv_handler.predict_site_median(
                cv_handler.train.iloc[:, train_indices], train_days, replace_nan=300)
            prediction = cv_handler.predict_from_1d(prediction, len(test_indices)).astype(int)
            score = cv_handler.smape(cv_handler.train.iloc[:, test_indices], prediction)
            current_median_scores.append(score)

            prediction = cv_handler.predict_site_mean(
                cv_handler.train.iloc[:, train_indices], train_days, replace_nan=300)
            prediction = cv_handler.predict_from_1d(prediction, len(test_indices)).astype(int)
            score = cv_handler.smape(cv_handler.train.iloc[:, test_indices], prediction)
            current_mean_scores.append(score)

            prediction = cv_handler.predict_site_log_mean(
                cv_handler.train.iloc[:, train_indices], train_days, replace_nan=300)
            prediction = cv_handler.predict_from_1d(prediction, len(test_indices)).astype(int)
            score = cv_handler.smape(cv_handler.train.iloc[:, test_indices], prediction)
            current_log_mean_scores.append(score)
        results.append([np.mean(current_median_scores), np.mean(current_mean_scores), np.mean(current_log_mean_scores)])

    for line in results:
        print(line)


main()

"""results"""
# train days range(10, 100, 10) median/mean/log mean
# [46.194528864602404, 48.269401261648532, 47.712203192498293]
# [45.605895180187396, 48.721324247175488, 47.542073060019035]
# [45.742318312519572, 49.113512621142739, 48.245298776918688]  # Used 30
# [46.478860503160625, 49.883225027836694, 49.606882953725226]
# [48.858233273594593, 50.552751648721518, 50.569875945801655]
# [49.779623207400604, 51.147970796985625, 51.337558683299839]
# [50.622023163527203, 51.676473138666111, 52.142894191007947]
# [51.382058291324192, 52.049436079273278, 52.684913294832086]
# [51.660089375037806, 52.549396133244443, 53.020740937866861]

# Change results to int
# [45.789381659634323, 48.490806717177861, 42.581632720153742]  # better to use int (probably around zero)
