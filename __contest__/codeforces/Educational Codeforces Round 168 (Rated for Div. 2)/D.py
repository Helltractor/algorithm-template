from types import GeneratorType

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
        n = II()
        g = [[] for _ in range(n)]
        a = LII()
        b = LII()
        for i, x in enumerate(b, 1):
            g[x - 1].append(i)

        def check(m):
            x = max(0, m - a[0])
            q = deque()
            for i in g[0]:
                q.append((i, x - min(0, a[i] - x)))
            while q:
                i, pre = q.pop()
                if len(g[i]) == 0:
                    if a[i] < pre:
                        return False
                    continue
                if pre > 10 ** 9:
                    return False
                for j in g[i]:
                    next_pre = pre - min(0, a[j] - pre)
                    q.append((j, next_pre))
            return True
        
        l = 0
        r = inf
        while l <= r:
            m = (l + r) // 2
            if check(m):
                l = m + 1
            else:
                r = m - 1
        print(r)
    return


if __name__ == '__main__':
    D()
