import pandas as pd
import datetime

from constants import DATE_FORMAT


class Test1Handler:
    def __init__(self, index_values, start_date, end_date):
        self.test1 = pd.DataFrame(data=0, index=index_values, columns=self.generate_dates_columns(start_date, end_date))

    @staticmethod
    def generate_dates_columns(start_date, end_date):
        dates = []
        current_date = datetime.datetime.strptime(start_date, DATE_FORMAT)
        end_date = datetime.datetime.strptime(end_date, DATE_FORMAT)
        while current_date <= end_date:
            dates.append(current_date.strftime(DATE_FORMAT))
            current_date = current_date + datetime.timedelta(days=1)
        return dates
