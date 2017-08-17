import pandas as pd
import numpy as np

from keyHandler import KeyHandler


class SubmissionHandler:
    def __init__(self, submission_filename, key_handler: KeyHandler):
        print('reading submission format')
        self.submission = pd.DataFrame.from_csv(submission_filename)
        self.key_handler = key_handler

    def save_prediction(self, test: pd.DataFrame, filename):
        print('saving submission')
        dates_hash = self.hash_dict(test.columns.values)
        pages_hash = self.hash_dict(test.index.values)

        ids = np.zeros(self.key_handler.key.shape[0]).astype(str)
        visits = np.zeros(self.key_handler.key.shape[0])

        for index, row in self.key_handler.key.iterrows():
            if not(index % 100000):
                print(index)
            ids[index] = row['Id']
            visits[index] = test.iat[pages_hash[row['Page']], dates_hash[row['Date']]]
        self.submission.index = ids
        self.submission['Visits'] = visits
        self.submission.Visits = self.submission.Visits.round(2)
        self.submission.index.name = 'Id'
        self.submission.to_csv(filename)

    @staticmethod
    def hash_dict(values):
        hash_dict = {}
        for i, value in enumerate(values):
            hash_dict[value] = i
        return hash_dict

# Id,Visits
# bf4edcf969af,0
# 929ed2bf52b9,0
# ff29d0f51d5c,0
# e98873359be6,0
# fa012434263a,0
