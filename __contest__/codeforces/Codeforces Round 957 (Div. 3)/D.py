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


def D():
    for _ in range(II()):
        n, m, k = MII()
        s = list(I())
        flag = True
        i = 0
        while i < n:
            while i < n and s[i] == 'L':
                i += 1
            j = i
            cnt = 0
            while i < n and s[i] != 'L':
                if s[i] == 'C':
                    cnt += 1
                i += 1
            if i - j < m:
                continue
            else:
                i = j + m - 1
                j = i
                cnt = 0
                while i < n and s[i] != 'L':
                    if s[i] == 'C':
                        cnt += 1
                    i += 1
                if cnt:
                    flag = False
                    break
                k -= i - j - cnt
                if k < 0:
                    flag = False
                    break
        print(Y if flag else N)
    return


if __name__ == '__main__':
    D()
