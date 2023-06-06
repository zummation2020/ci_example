import unittest
from task import conv_endian


class TestConvEndian(unittest.TestCase):

    def test_conv_endian1(self):
        self.assertEqual(conv_endian(954786, 'big'), '0E 91 A2')

    def test_conv_endian2(self):
        self.assertEqual(conv_endian(954786), '0E 91 A2')


if __name__ == '__main__':
    unittest.main()
