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
    n, s, t = MII()
    a = LII()
    b = LII()
    c = [(x, y) for x, y in zip(a, b)]
    c.sort(key=lambda x: -x[0])
    ss = s
    tt = t
    cnt1 = n
    for i, (x, y) in enumerate(c, 1):
        ss -= x
        tt -= y
        if ss < 0 or tt < 0:
            cnt1 = i
            break
    c.sort(key=lambda x: -x[1])
    ss = s
    tt = t
    cnt2 = n
    for i, (x, y) in enumerate(c, 1):
        ss -= x
        tt -= y
        if ss < 0 or tt < 0:
            cnt2 = i
            break
    print(min(cnt1, cnt2))
    return


if __name__ == '__main__':
    C()
