import unittest
import argparse
from main import sumMax


class TestSumMax(unittest.TestCase):

    def setUp(self):
        pass

    def test_max_3_4_7(self):
        self.assertEqual(sumMax('3 4 7'.split()), 7)

    def test_max_n3_4_2(self):
        self.assertEqual(sumMax('-3 4 2'.split()), 4)

    def test_sum_3_4_8(self):
        self.assertEqual(sumMax('3 4 8 --sum'.split()), 15)

    def test_sum_3_4_8p2(self):
        self.assertEqual(sumMax('3 4 8.2 --sum'.split()), 15.2)


if __name__ == '__main__':
    unittest.main()
