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

# https://codeforces.com/problemset/problem/1905/C
def CF1905C():
    for _ in range(II()):
        n = II()
        a = list(I())
        b = sorted(a)
        if a == b:
            print(0)
            continue
        st = []
        for i, c in enumerate(a):
            while st and a[st[-1]] < c:
                st.pop()
            st.append(i)
        c = a[:]
        for i in range(len(st) // 2):
            c[st[i]], c[st[-i - 1]] = c[st[-i - 1]], c[st[i]]
        if c != b:
            print(-1)
            continue
        m = len(st)
        for i in st:
            if a[i] == a[st[0]]:
                m -= 1
        print(m)
    return


if __name__ == '__main__':
    CF1905C()
