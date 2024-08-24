# _*_ coding: utf-8 _*_
# @File : primes_factor.py
# @Time : 2023/11/30 19:19
# @Author : Helltractor
from collections import Counter

from typing import List


class PrimesFactor:
    
    @staticmethod
    def count_primes_factor(n: int) -> int:
        """ 统计每个数的质因子的个数"""
        
        cnt = [0] * n
        for i in range(2, n):
            if cnt[i] == 0:
                for j in range(i, n, i):
                    cnt[j] += 1
        return cnt
    
    @staticmethod
    def primes_factor(n: int) -> List[List[int]]:
        """统计每个数的质因子"""
        
        fac = [[] for _ in range(n)]
        for i in range(2, n):
            if not fac[i]:
                for j in range(i, n, i):
                    fac[j].append(i)
        return fac
    
    @staticmethod
    def prime_factor(n: int) -> Counter:
        """
            统计一个数的质因子个数
            a = p1 ^ e1 * p2 ^ e2 * p3 ^ e3
        """
        cnt = Counter()
        d = 2
        while d * d <= n:
            while n % d == 0:
                cnt[d] += 1
                n //= d
            d += 1
        if n > 1:
            cnt[n] += 1
        return cnt
    