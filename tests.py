import unittest
from task import my_datetime

class MyDatetimeTestCase(unittest.TestCase):

    def test_epoch(self):
        num_sec = 0
        expected = '01-01-1970'
        self.assertEqual(my_datetime(num_sec), expected)

    def test_1to9(self):
        num_sec = 123456789
        expected = '11-29-1973'
        self.assertEqual(my_datetime(num_sec), expected)

    def test_9to0(self):
        num_sec = 9876543210
        expected = '12-22-2282'
        self.assertEqual(my_datetime(num_sec), expected)

    def test_large_date(self):
        num_sec = 201653971200
        expected = '02-29-8360'
        self.assertEqual(my_datetime(num_sec), expected)


if __name__ == '__main__':
    unittest.main()
