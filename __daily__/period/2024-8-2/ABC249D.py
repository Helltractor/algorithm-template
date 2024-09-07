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

# https://atcoder.jp/contests/abc249/tasks/abc249_d
def ABC249D():
    n = II()
    a = LII()
    cnt = Counter(a)
    ans = 0
    # for k, v in cnt.items():
    #     for i in range(1, k + 1):
    #         if k % i == 0:
    #             ans += v * cnt[i] * cnt[k // i]
    # print(ans)
    
    mx = 2 * 10 ** 5
    for i in range(1, mx + 1):
        for j in range(1, mx // i + 1):
            ans += cnt[i] * cnt[j] * cnt[i * j]
    print(ans)
    return


if __name__ == '__main__':
    ABC249D()
