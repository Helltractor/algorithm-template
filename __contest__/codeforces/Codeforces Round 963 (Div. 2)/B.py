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


def B():
    for _ in range(II()):
        n = II()
        a = LII()
        a.sort()
        odd = sum(x % 2 for x in a)
        even = n - odd
        if odd == 0 or even == 0:
            print(0)
            continue
        odds = [x for x in a if x % 2]
        evens = [x for x in a if x % 2 == 0]
        pre = odds[-1]
        ans = 0
        # print(pre, evens)
        for x in evens:
            y = x + pre
            if x > pre:
                ans += 1
                y = y + x
            pre = max(y, pre)
            ans += 1
        print(min(ans, even + 1))
    return


if __name__ == '__main__':
    B()
