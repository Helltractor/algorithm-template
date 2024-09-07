import unittest

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
        
def CF1935C():
    for _ in range(II()):
        n, l = MII()
        arr = []
        flag = True
        for _ in range(n):
            a, b = MII()
            arr.append([a, b])
            if a <= l:
                flag = False
        if flag:
            print(0)
        else:
            ans = 1
            arr.sort(key=lambda x: x[1])
            # for i, (x, y) in enumerate(arr):
            #     h = []
            #     s = 0
            #     for j in range(i - 1, -1, -1):
            #         if x + y - arr[j][1] > l:
            #             break
            #         s += arr[j][0]
            #         heappush(h, -arr[j][0])
            #         while h and x + y - arr[j][1] + s > l:
            #             s += heappop(h)
            #         ans = max(ans, len(h) + 1)
            # print(ans)
            dp = [inf] * n
            for i in range(n):
                dp[i] = arr[i][0] - arr[i][1]
            for i in range(1, n):
                mn = dp[i - 1]
                for j in range(i, n):
                    pre = dp[j]
                    dp[j] = mn + arr[j][0]
                    if dp[j] + arr[j][1] <= l:
                        ans = i + 1
                    mn = min(mn, pre)
            print(ans)
    return


if __name__ == '__main__':
    CF1935C()
