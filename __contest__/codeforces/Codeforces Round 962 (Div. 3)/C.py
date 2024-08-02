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


def C():
    for _ in range(II()):
        n, q = MII()
        a = I()
        b = I()
        cntA = [[0] * 26 for _ in range(n + 1)]
        cntB = [[0] * 26 for _ in range(n + 1)]
        for i, (x, y) in enumerate(zip(a, b)):
            cntA[i + 1] = cntA[i][:]
            cntB[i + 1] = cntB[i][:]
            cntA[i + 1][ord(x) - 97] = cntA[i][ord(x) - 97] + 1
            cntB[i + 1][ord(y) - 97] = cntB[i][ord(y) - 97] + 1
        for _ in range(q):
            l, r = MII()
            tmpA = [cntA[r][i] - cntA[l - 1][i] for i in range(26)]
            tmpB = [cntB[r][i] - cntB[l - 1][i] for i in range(26)]
            s = 0
            for i in range(26):
                s += abs(tmpA[i] - tmpB[i])
            print(s // 2)
    return


if __name__ == '__main__':
    C()
