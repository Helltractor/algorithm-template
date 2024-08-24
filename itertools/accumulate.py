# _*_ coding: utf-8 _*_
# @File : accumulate.py
# @Time : 2024/5/3 14:53

import operator
import unittest


class MyTestCase(unittest.TestCase):
    def test_accumulate(self):
        self.assertEqual(list(accumulate(range(10))), [0, 1, 3, 6, 10, 15, 21, 28, 36, 45])
        self.assertEqual(list(accumulate(range(10), initial=1)), [1, 1, 2, 4, 7, 11, 16, 22, 29, 37, 46])
        self.assertEqual(list(accumulate(range(10), operator.mul)), [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.assertEqual(list(accumulate(range(10), operator.mul, initial=1)), [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


def accumulate(iterable, func=operator.add, *, initial=None):
    """Return running totals"""
    it = iter(iterable)
    total = initial
    if initial is None:
        try:
            total = next(it)
        except StopIteration:
            return
    yield total
    for element in it:
        total = func(total, element)
        yield total

if __name__ == "__main__":
    unittest.main()
    