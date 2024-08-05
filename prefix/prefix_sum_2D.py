# _*_ coding: utf-8 _*_
# @File : prefix_sum_2D.py
# @Time : 2023/12/14 13:13
# @Author : Helltractor
from typing import List


class PrefixSum2D:
    def __init__(self, mat: List[List[int]]):
        n, m = len(mat), len(mat[0])
        self.pre = pre = [[0] * (m + 1) for _ in range(n + 1)]
        for i, row in enumerate(mat):
            for j, v in enumerate(row):
                pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + v

    def find(self, r1: int, c1: int, r2: int, c2: int) -> int:
        """查询以(r1,c1)为左上角，(r2,c2)为右下角的矩形区间内所有值的和"""
        pre = self.pre
        return pre[r2 + 1][c2 + 1] - pre[r2 + 1][c1] - pre[r1][c2 + 1] + pre[r1][c1]
