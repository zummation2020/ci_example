import unittest
from task import conv_num
from task import my_datetime
from task import conv_endian

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

class TestConvEndian(unittest.TestCase):

    def test_conv_endian1(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_conv_endian2(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')


class ConvNumTestCase(unittest.TestCase):

    def test_positive_integer(self):
        num_str = '12345'
        expected = 12345
        self.assertEqual(conv_num(num_str), expected)

    def test_negative_integer(self):
        num_str = '-54321'
        expected = -54321
        self.assertEqual(conv_num(num_str), expected)

    def test_under_one(self):
        num_str = '.45'
        expected = 0.45
        self.assertEqual(conv_num(num_str), expected)

    def test_no_num_after_decimal(self):
        num_str = '123.'
        expected = 123.0
        self.assertEqual(conv_num(num_str), expected)

    def test_positive_float(self):
        num_str = '123.45'
        expected = 123.45
        self.assertEqual(conv_num(num_str), expected)

    def test_negative_float(self):
        num_str = '-123.45'
        expected = -123.45
        self.assertEqual(conv_num(num_str), expected)

    def test_float_with_multiple_decimal_points(self):
        num_str = '12.34.56'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_hexadecimal_number(self):
        num_str = '0xAD4'
        expected = 2772
        self.assertEqual(conv_num(num_str), expected)

    def test_invalid_hexadecimal_number(self):
        num_str = '0xAZ4'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_invalid_input_type(self):
        num_str = '12345A'
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_empty_string(self):
        num_str = ''
        expected = None
        self.assertEqual(conv_num(num_str), expected)

    def test_multiple_decimal(self):
        num_str = '12.3.45'
        expected = None
        self.assertEqual(conv_num(num_str), expected)


if __name__ == '__main__':
    unittest.main()
