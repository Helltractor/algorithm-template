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

# 不相较区间（递增元素的分布区间）的连续个数
def cf_1167E():
    n, x = MII()
    a = LII()
    ps = [[inf, 0, i] for i in range(x + 1)]
    for i, c in enumerate(a, 1):
        if ps[c][0] == inf:
            ps[c][0] = i
        ps[c][1] = i
        
    b = [p for p in ps if p[1]]
    m = len(b)
    i = 0
    while i < m - 1 and b[i][1] < b[i + 1][0]:
        i += 1
    if i == m - 1:
        print(x * (x + 1) // 2)
        return
    
    # 去掉后缀 b[<=i+1] ~ b[n-1]
    ans = b[i + 1][-1] * (x + 1 - b[-1][-1])
    j = m - 1
    while j == m - 1 or b[j][1] < b[j + 1][0]:
        while i >= 0 and b[j][0] <= b[i][1]:
            i -= 1
        # 去掉 b[<=i+1] ~ b[j-1]
        ans += b[i + 1][-1] * (b[j][-1] - b[j - 1][-1])
        j -= 1
    print(ans)
    return


if __name__ == '__main__':
    cf_1167E()
