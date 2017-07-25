import pandas as pd


class KeyHandler:
    def __init__(self, key_filename):
        self.key = pd.DataFrame.from_csv(key_filename)
        print(self.key)
