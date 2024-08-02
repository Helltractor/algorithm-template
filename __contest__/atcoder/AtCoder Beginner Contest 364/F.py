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


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = list(range(n))
        self.rank = [1] * n
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union_by_size(self, x, y):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.size[y_root] <= self.size[x_root]:
                self.parent[y_root] = x_root
                self.size[x_root] += self.size[y_root]
            else:
                self.parent[x_root] = y_root
                self.size[y_root] += self.size[x_root]
    
    def union_rank(self, x: int, y: int):
        x_root, y_root = self.find(x), self.find(y)
        if x_root != y_root:
            if self.rank[y_root] <= self.rank[x_root]:
                self.parent[y_root] = x_root
            else:
                self.parent[x_root] = y_root
            if self.rank[x_root] == self.rank[y_root]:
                self.rank[x_root] += 1
    
    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)
    
def F():
    n, q = MII()
    uf = UnionFind(n + q + 1)
    h = []
    g = [[inf] * (n + q + 1) for _ in range(n + q + 1)]
    for i in range(1, q + 1):
        l, r, c = MII()
        for j in range(l, r + 1):
            g[n + i][j] = min(g[n + i][j], c)
            g[j][n + i] = g[n + i][j]
            if uf.connected(j, n + i):
                continue
            uf.union_by_size(j, n + i)
    if max(uf.size) == n + q:
        vis = set()
        for i in range(1, n + q + 1):
            for j in range(i + 1, n + q + 1):
                if g[i][j] < inf:
                    heappush(h, (g[i][j], i, j))
        ans = 0
        while h and len(vis) < n + q:
            c, l, r = heappop(h)
            if l in vis and r in vis:
                continue
            vis.add(l)
            vis.add(r)
            ans += c
        print(ans)
    else:
        print(-1)
    return


if __name__ == '__main__':
    F()
