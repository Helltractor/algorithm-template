import unittest

ImportType = InputType = ConstType = 1
if ImportType:
    import os, sys, random, threading
    from random import randint, choice, shuffle
    from copy import deepcopy
    from functools import lru_cache, reduce
    from bisect import bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    from heapq import heapify, heappop, heappush, heappushpop
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, comb, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
    from decimal import Decimal, getcontext
    from sys import stdin, stdout, setrecursionlimit

if InputType:
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    I = lambda: input()
    II = lambda: int(input())
    MII = lambda: map(int, input().split())
    LI = lambda: list(input().split())
    LII = lambda: list(map(int, input().split()))
    GMI = lambda: map(lambda x: int(x) - 1, input().split())
    LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD = 998244353
    inf = 10 ** 18
    Y = "Yes"
    N = "No"

class UnitTest(unittest.TestCase):
    
    def solve(self, n, a):
        def f(n, a):
            sm = sum(a)
            b = [0] * n
            cnt = [0] * (n + 1)
            mad = 0
            for i in range(n):
                cnt[a[i]] += 1
                if cnt[a[i]] >= 2:
                    mad = max(mad, a[i])
                b[i] = mad
            return sm, b
        
        ans = 0
        sm, b = f(n, a)
        ans += sm
        sm, b = f(n, b)
        ans += sm
        tmp = 0
        for i in range(n):
            diff = b[i] - tmp
            c = (n - i)
            ans += diff * c * (c + 1) // 2
            tmp = b[i]
        return ans
    
    def solve1(self, n, a):
        def f(a):
            s = sum(a)
            cnt = [0] * (n + 1)
            mad = 0
            for i in range(n):
                cnt[a[i]] += 1
                if cnt[a[i]] >= 2:
                    mad = max(mad, a[i])
                a[i] = mad
            return s, a
        s1, b = f(a)
        s2, b = f(b)
        pre = 0
        ans = s1 + s2
        cnt = Counter(b)
        for x in sorted(cnt, reverse=True):
            v = cnt[x]
            ans += (v * pre + (v + 1) * v // 2) * x
            pre += v
        return ans
    
    def test(self):
        for i in range(1, 100):
            n = random.randint(1, 10000)
            a = [random.randint(1, n) for _ in range(n)]
            other = self.solve(n, a)
            my = self.solve1(n, a)
            assert other == my
        return


def C():
    for _ in range(II()):
        n = II()
        a = LII()
        def f(a):
            s = sum(a)
            cnt = [0] * (n + 1)
            mad = 0
            for i in range(n):
                cnt[a[i]] += 1
                if cnt[a[i]] >= 2:
                    mad = max(mad, a[i])
                a[i] = mad
            return s, a
        s1, b = f(a)
        s2, b = f(b)
        pre = 0
        ans = s1 + s2
        cnt = Counter(b)
        for x in sorted(cnt, reverse=True):
            v = cnt[x]
            ans += (v * pre + (v + 1) * v // 2) * x
            pre += v
        print(ans)
    return


if __name__ == '__main__':
    C()
