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

# x ** a < y ** b
# a * log(x, 2) < b * log(y, 2)
# log(a, 2) + log(log(x, y), 2) < log(b, 2)
def C():
    for _ in range(II()):
        n = II()
        a = LII()
        ans = 0
        dp = [0] * n
    
        for i, x in enumerate(a[1:], 1):
            if x == 1:
                if a[i - 1] > x:
                    ans = -1
                    break
                continue
            b = log(a[i - 1], x)
            # c = max(0, dp[i - 1] + int(log2(int(b + 1))) - 5)
            c = max(0, dp[i - 1] + int(b + 1).bit_length() - 5)
            while pow(2, c - dp[i - 1]) < b:
                c += 1
            dp[i] = c
            ans += dp[i]
        print(ans)
    return


if __name__ == '__main__':
    C()
