# _*_ coding: utf-8 _*_
# @File : difference.py
# @Time : 2023/9/29 16:52
# @Author : Helltractor

from typing import List

class Difference:
    
    @staticmethod
    def diff_array(n: int, queries: List[List[int]]) -> List[int]:
        diff = [0] * (n + 1)
        for left, right, delta in queries:
            diff[left] += delta
            diff[right + 1] -= delta
        for i in range(1, n):
            diff[i] += diff[i - 1]
        return diff[:-1]
