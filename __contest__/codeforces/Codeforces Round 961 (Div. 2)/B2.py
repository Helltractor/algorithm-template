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
    
def B2():
    for _ in range(II()):
        n, m = MII()
        a = LII()
        c = LII()
        cnt = Counter()
        for x, y in zip(a, c):
            cnt[x] = y
        res = 0
        for k, v in cnt.items():
            if k > m:
                continue
            pre, mod = divmod(m, k)
            cnt1 = min(pre, v)
            mod = m - cnt1 * k
            suf, mod2 = divmod(mod, k + 1)
            cnt2 = min(cnt[k + 1], suf)
            mod2 = mod - cnt2 * (k + 1)
            res = max(res, cnt1 * k + cnt2 * (k + 1) + min(cnt1, cnt[k + 1] - cnt2, mod2))
        print(res)
    return


if __name__ == '__main__':
    B2()
