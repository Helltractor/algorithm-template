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


def cf_1725M():
    # n, m = MII()
    # g = [[] for _ in range(n)]
    # for _ in range(m):
    #     u, v, w = MII()
    #     u -= 1
    #     v -= 1
    #     g[u].append((v, w, 0))
    #     g[v].append((u, w, 1))
    # dis = [[inf] * 2 for _ in range(n)]
    # dis[0] = [0, 0]
    # h = [(0, 0, 0)]
    # while h:
    #     d, u, uInv = heappop(h)
    #     if d > dis[u][uInv]:
    #         continue
    #     for v, w, vInv in g[u]:
    #         nd = d + w
    #         if (vInv or uInv == 0) and dis[v][vInv] > nd:
    #             dis[v][vInv] = nd
    #             heappush(h, (nd, v, vInv))
    # ans = [-1] * (n - 1)
    # for i, row in enumerate(dis[1:]):
    #     tmp = min(row)
    #     if tmp < inf:
    #         ans[i] = tmp
    # print(*ans)
    
    n, m = MII()
    # 状态转移，选择反向边
    g = [[(u + n, 0)] if u <= n else [] for u in range(n << 1 | 1)]
    for _ in range(m):
        u, v, w = MII()
        g[u].append((v, w))
        g[v + n].append((u + n, w))
    dis = [inf] * (n << 1 | 1)
    dis[1], mask, h = 0, (1 << 20) - 1, [1]
    while h:
        s = heappop(h)
        d, u = s >> 20, s & mask
        if d > dis[u]:
            continue
        for v, w in g[u]:
            new_d = w + d
            if new_d < dis[v]:
                dis[v] = new_d
                heappush(h, new_d << 20 | v)
    print(' '.join(map(lambda x: str(x) if x < inf else '-1', dis[n + 2:])))
    return


if __name__ == '__main__':
    cf_1725M()
