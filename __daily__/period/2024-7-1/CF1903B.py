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


def CF1903B():
    for _ in range(II()):
        n = II()
        g = [LII() for _ in range(n)]
        a = [(1 << 30) - 1] * n
        flag = True
        for i in range(n - 1):
            for j in range(i + 1, n):
                a[i] &= g[i][j]
        for j in range(n - 1, 0, -1):
            for i in range(j):
                a[j] &= g[i][j]
        for i in range(n):
            for j in range(n):
                if i != j and a[i] | a[j] != g[i][j]:
                    flag = False
                    break
        if flag:
            print("YES")
            print(*a)
        else:
            print("NO")
    return


def main():
    CF1903B()
    return


if __name__ == '__main__':
    main()
