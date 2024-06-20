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
        b = -2
        co = 0
        for i in range(0, n):
            if a[i] == 0:
                b = -2
            elif b == 0:
                if a[i] <= 2:
                    b = -2
                elif a[i] <= 4:
                    b = 2
                    co += 1
                else:
                    b = -2
                    co += 1
            elif a[i] <= 2 or (b == 2 and a[i] <= 4):
                b = 0
                co += 1
            else:
                b = -2
                co += 1
        return co
    
    def mysolve(self, n, a):
        
        ans = 0
        pre = 0
        for i, x in enumerate(a):
            if x == 0:
                pre = 0
            elif pre == 1:
                if x <= 2:
                    pre = 0
                elif x <= 4:
                    pre = 2
                    ans += 1
                else:
                    pre = 0
                    ans += 1
            elif x <= 2 or (pre == 2 and x <= 4):
                pre = 1
                ans += 1
            else:
                pre = 0
                ans += 1
        return ans

    def test(self):
        for _ in range(10 ** 5):
            n = randint(1, 10)
            a = [randint(1, n) for _ in range(n)]
            other = self.solve(n, a)
            mine = self.mysolve(n, a)
            if other != mine:
                print(n)
                print(a)
            assert other == mine, (other, mine)
        return

# pre = 0 : no square
# pre = 1 : one square (0, 2)
# pre = 2 : one square (2, 4)
def D():
    for _ in range(II()):
        n = II()
        a = LII()
        
        ans = 0
        pre = 0
        for i, x in enumerate(a):
            if x == 0:
                pre = 0
            elif pre == 1:
                if x <= 2:
                    pre = 0
                elif x <= 4:
                    pre = 2
                    ans += 1
                else:
                    pre = 0
                    ans += 1
            elif x <= 2 or (pre == 2 and x <= 4):
                pre = 1
                ans += 1
            else:
                pre = 0
                ans += 1
        print(ans)
    return


if __name__ == '__main__':
    D()
