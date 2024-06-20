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

def test():
    for _ in range(10000):
        n = randint(1, 100)
        x = randint(1, n)
        y = randint(1, n)
        if x <= y:
            continue
        print(n, x, y)
        a = [1] * n
        flag = True
        for i in range(x, n):
            if flag:
                a[i] = -1
            flag = not flag
        
        for i in range(y - 1):
            a[i] = -1
            if flag:
                a[i] = -1
            flag = not flag
        pre = [0] * n
        for i in range(n):
            pre[i] = pre[i - 1] + a[i]
        suf = [0] * n
        for i in range(n - 1, -1, -1):
            suf[i] = suf[(i + 1) % n] + a[i]
        print(pre)
        print(suf)
        print(*a)
        print()
        
def B():
    for _ in range(II()):
        n, x, y = MII()
        a = [1] * n
        flag = True
        for i in range(x, n):
            if flag:
                a[i] = -1
            flag = not flag
        flag = True
        for i in range(y - 2, -1, -1):
            if flag:
                a[i] = -1
            flag = not flag
        print(*a)
    return


if __name__ == '__main__':
    B()
    # test()