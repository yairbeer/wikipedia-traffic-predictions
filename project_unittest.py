import unittest

from keyHandler import KeyHandler
from submissionHandler import SubmissionHandler
from trainHandler import TrainHandler
from test1Handler import Test1Handler


class TestProjectMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('start')

    def test_generate_dates_test_1(self):
        self.assertEqual(len(Test1Handler.generate_dates_columns('2017-01-01', '2017-03-01')), 60)

    @classmethod
    def tearDownClass(cls):
        print('end')

if __name__ == '__main__':
    unittest.main()
