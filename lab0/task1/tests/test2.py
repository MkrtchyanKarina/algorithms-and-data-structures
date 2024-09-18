import unittest

from lab0.task1.src.task2 import sum_ab2


class Sum_ab2_test(unittest.TestCase):
    def test_sum_ab2(self):
        self.assertEqual(sum_ab2("130 61", 0), 3851)
        self.assertEqual(sum_ab2("12 -25", 0), 637)
        self.assertEqual(sum_ab2("-25 4", 0), -9)