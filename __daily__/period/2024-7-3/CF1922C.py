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


def CF1922C():
    for _ in range(II()):
        n = II()
        a = LII()
        l = [0] * n
        r = [0] * n
        
        l[1] = 1
        r[-2] = 1
        for i in range(1, n - 1):
            x = a[i] - a[i - 1]
            y = a[i + 1] - a[i]
            if x > y:
                l[i + 1] = l[i] + 1
            else:
                l[i + 1] = l[i] + y
        
        for i in range(n - 2, 0, -1):
            x = a[i] - a[i - 1]
            y = a[i + 1] - a[i]
            if x > y:
                r[i - 1] = r[i] + x
            else:
                r[i - 1] = r[i] + 1
        
        for _ in range(II()):
            x, y = GMI()
            if x > y:
                print(r[y] - r[x])
            else:
                print(l[y] - l[x])
    return


if __name__ == '__main__':
    CF1922C()
