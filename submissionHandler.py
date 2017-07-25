import pandas as pd

from keyHandler import KeyHandler


class SubmissionHandler:
    def __init__(self, submission_filename, key_handler: KeyHandler):
        self.submission = pd.DataFrame.from_csv(submission_filename)

# Id,Visits
# bf4edcf969af,0
# 929ed2bf52b9,0
# ff29d0f51d5c,0
# e98873359be6,0
# fa012434263a,0
