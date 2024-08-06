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

def modinv(a, p):
    return pow(a, p - 2, p)

def precompute_combinations(n, mod):
    fac = [1] * (n + 1)
    inv_fac = [1] * (n + 1)
    for i in range(2, n + 1):
        fac[i] = fac[i - 1] * i % mod
    inv_fac[n] = modinv(fac[n], mod)
    for i in range(n - 1, 0, -1):
        inv_fac[i] = inv_fac[i + 1] * (i + 1) % mod
    return fac, inv_fac

def comb(n, k):
    if k > n or k < 0:
        return 0
    return fac[n] * inv_fac[k] % mod * inv_fac[n - k] % mod

mod = 10 ** 9 + 7
fac, inv_fac = precompute_combinations(2 * 10 ** 5 + 5, mod)
def F():
    for _ in range(II()):
        n, k = MII()
        a = LII()
        ans = 0
        s = sum(a)
        for j in range(k // 2 + 1, min(s, k) + 1):
            ans += comb(s, j) * comb(n - s, k - j) % mod
        print(ans % mod)
    return


if __name__ == '__main__':
    F()
