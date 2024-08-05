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
    sys.setrecursionlimit(20000)
    
if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD = 998244353
    inf = 10 ** 18
    Y = "Yes"
    N = "No"
    
# class MyTest(unittest.TestCase):
#
#     def testcase(self):
#         for _ in range(10000):
#             n = randint(1, 1000)
#             k = randint(1, 11)
#             s = "".join([choice("AB?") for _ in range(n)])
#             self.assertEqual(self.my_solve(n, k, s), self.correct_solve(n, k, s))
#         return
#
#     def my_solve(self, n, k, s):
#         pal = [False] * (1 << k)
#         for i in range(len(pal)):
#             for j in range(k // 2):
#                 if (i >> j) & 1 != (i >> (k - 1 - j)) & 1:
#                     break
#             else:
#                 pal[i] = True
#
#         mask = (1 << (k - 1)) - 1
#         @lru_cache(None)
#         def dfs(i, j):
#             if i < 0:
#                 return 1
#             res = 0
#             for b in range(2):
#                 if s[i] != '?' and (ord(s[i]) - ord('A')) != b:
#                     continue
#                 tmp = (j << 1) | b
#                 if i > n - k or (not pal[tmp]):
#                     res += dfs(i - 1, tmp & mask)
#             res %= MOD
#             return res
#         ans = dfs(n - 1, 0)
#         # print(dfs(n - 1, 0))
#         return ans
#
#     def correct_solve(self, n, k, s):
#         mod = 998244353
#         pal = [False] * (1 << k)
#         for i in range(1 << k):
#             f = False
#             for j in range(k // 2):
#                 if (1 << j) & i == 0 and (1 << (k - j - 1)) & i > 0:
#                     f = True
#                     break
#                 if (1 << j) & i > 0 and (1 << (k - j - 1)) & i == 0:
#                     f = True
#                     break
#             if not f:
#                 pal[i] = True
#
#         mask = (1 << (k - 1)) - 1
#         @lru_cache(None)
#         def dfs(x: int, y: int) -> int :
#             if x < 0:
#                 return 1
#             res = 0
#             for b in range(2):
#                 if s[x] != '?' and (ord(s[x]) - ord('A')) != b:
#                     continue
#                 t = (y << 1) | b
#                 if x > n - k or (not pal[t]):
#                     res += dfs(x-1, t & mask)
#
#             res %= mod
#             return res
#         ans = dfs(n-1, 0)
#         return ans
    
# https://atcoder.jp/contests/abc359/tasks/abc359_d
def abc_359D():
    n, k = MII()
    s = I()
    
    pal = [False] * (1 << k)
    for i in range(len(pal)):
        for j in range(k // 2):
            if (i >> j) & 1 != (i >> (k - 1 - j)) & 1:
                break
        else:
            pal[i] = True
        
    mask = (1 << (k - 1)) - 1
    @lru_cache(None)
    def dfs(i, j):
        if i < 0:
            return 1
        res = 0
        for b in range(2):
            if s[i] != '?' and s[i] != chr(b + 65):
                continue
            tmp = j << 1 | b
            if i > n - k or not pal[tmp]:
                res += dfs(i - 1, tmp & mask)
        res %= MOD
        return res
    print(dfs(n - 1, 0))
    return


if __name__ == '__main__':
    abc_359D()
