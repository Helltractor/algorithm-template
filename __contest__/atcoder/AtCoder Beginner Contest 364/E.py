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


def E():
    n, s, t = MII()
    c = []
    for _ in range(n):
        a, b = MII()
        c.append((a, b))
    dp = [[[inf] * (s + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    dp[0][0][0] = 0
    for i in range(n):
        for j in range(n):
            for k in range(s + 1):
                dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
                if dp[i + 1][j][k] == inf:
                    continue
                if k + c[i][0] <= s:
                    dp[i + 1][j + 1][k + c[i][0]] = min(dp[i + 1][j + 1][k + c[i][0]], dp[i][j][k] + c[i][1])
    for i in range(n, -1, -1):
        for j in range(s + 1):
            if dp[n][i][j] <= t:
                ans = min(i + 1, n)
                print(ans)
                return 0
    return -1


if __name__ == '__main__':
    E()
