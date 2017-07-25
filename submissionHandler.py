import pandas as pd

from keyHandler import KeyHandler


class SubmissionHandler:
    def __init__(self, submission_filename, key_handler: KeyHandler):
        self.submission = pd.DataFrame.from_csv(submission_filename)
        self.key_handler = key_handler

    def save_prediction(self, test: pd.DataFrame, filename):
        dates_hash = self.hash_dict(test.columns.values)
        pages_hash = self.hash_dict(test.index.values)
        for line in self.key_handler.key:
            value = test.iat[pages_hash[line['page']], dates_hash[line['date']]]
            self.submission.at[line['key']] = value
        self.submission.to_csv(filename)

    @staticmethod
    def hash_dict(values):
        hash_dict = {}
        for i, value in values:
            hash_dict[value] = i
        return hash_dict

# Id,Visits
# bf4edcf969af,0
# 929ed2bf52b9,0
# ff29d0f51d5c,0
# e98873359be6,0
# fa012434263a,0
