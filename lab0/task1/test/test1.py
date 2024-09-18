import unittest

from lab0.task1.src.task1 import sum_ab


class Sum_ab_test(unittest.TestCase):
    def test_sum_ab(self):
        self.assertEqual(sum_ab("130 61", 0), 191)
        self.assertEqual(sum_ab("130 -150", 0), -20)
        self.assertEqual(sum_ab("12 25", 0), 37)

