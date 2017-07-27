import pandas as pd


class KeyHandler:
    def __init__(self, key_filename):
        print('reading key')
        self.key = pd.read_csv(key_filename, header=0)
        print('parsing key page')
        self.parse_page()

    def parse_page(self):
        self.key['Date'] = self.key['Page'].map(lambda string: string[-10:])
        self.key['Page'] = self.key['Page'].map(lambda string: string[:-11])

# "Page","Id"
# "!vote_en.wikipedia.org_all-access_all-agents_2017-01-01",bf4edcf969af
# "!vote_en.wikipedia.org_all-access_all-agents_2017-01-02",929ed2bf52b9
