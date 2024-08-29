ImportType = InputType = ConstType = 1
if ImportType:
    import os, sys, random, threading
    from random import randint, choice, shuffle
    from copy import deepcopy
    from io import BytesIO, IOBase
    from types import GeneratorType
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


def cf_1849D():
    n = II()
    a = LII()
    ans = 0
    i = 0
    while i < n:
        if a[i] == 0:
            ans += 1
            i += 1
            continue
        j = i
        has = False
        while i < n and a[i]:
            # 修改两个端点
            if a[i] == 2:
                has = True
            i += 1
        ans += 1
        # 左端点
        if j > 0 and a[j - 1] == 0:
            ans -= 1
            if not has:
                continue
        # 右端点
        if i < n:
            a[i] = 1
            i += 1
    print(ans)
    return


def main():
    cf_1849D()
    return


if __name__ == '__main__':
    main()
