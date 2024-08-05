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
        a = list(I())
        b = list(I())
        i = 0
        j = 0
        ans = []
        while i < len(a) and j < len(b):
            if a[i] != '?':
                ans.append(a[i])
                if a[i] == b[j]:
                    j += 1
            else:
                ans.append(b[j])
                j += 1
            i += 1
        while i < len(a):
            if a[i] != '?':
                ans.append(a[i])
            else:
                ans.append('a')
            i += 1
        if j == len(b):
            print(Y)
            print(''.join(ans))
        else:
            print(N)
    return


if __name__ == '__main__':
    D()
