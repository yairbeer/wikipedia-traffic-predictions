import unittest

from keyHandler import KeyHandler
from submissionHandler import SubmissionHandler
from trainHandler import TrainHandler


class TestProjectMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        key_handler = KeyHandler('key_1.csv')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
