ImportType = InputType = ConstType = 1
DecoratorType = FunctinoType = 1
if ImportType:
    import os, sys, random, threading
    from copy import deepcopy
    from decimal import Decimal, getcontext
    from random import randint, choice, shuffle
    from types import GeneratorType
    from functools import lru_cache, reduce
    from bisect import bisect_left, bisect_right
    from collections import Counter, defaultdict, deque
    from itertools import accumulate, combinations, permutations
    from heapq import heapify, heappop, heappush, heappushpop
    from typing import Generic, Iterable, Iterator, TypeVar, Union, List
    from string import ascii_lowercase, ascii_uppercase, digits
    from math import ceil, comb, floor, sqrt, pi, factorial, gcd, log, log10, log2, inf
    from sys import stdin, stdout, setrecursionlimit

if InputType:
    input = lambda: sys.stdin.readline().rstrip("\r\n")
    I = lambda: input()
    II = lambda: int(input())
    MII = lambda: map(int, input().split())
    LI = lambda: list(input())
    LII = lambda: list(map(int, input().split()))
    GMI = lambda: map(lambda x: int(x) - 1, input().split())
    LGMI = lambda: list(map(lambda x: int(x) - 1, input().split()))

if DecoratorType:
    def bootstrap(f, stack=[]):
        def wrappedfunc(*args, **kwargs):
            if stack:
                return f(*args, **kwargs)
            else:
                to = f(*args, **kwargs)
                while True:
                    if type(to) is GeneratorType:
                        stack.append(to)
                        to = next(to)
                    else:
                        stack.pop()
                        if not stack: break
                        to = stack[-1].send(to)
                return to
        
        return wrappedfunc

if FunctinoType:
    class Math:
        __slots__ = ["mod", "l", "fact", "inv"]
        
        def __init__(self):
            self.mod = mod = 10 ** 9 + 7
            self.l = l = 3 * 10 ** 5 + 5
            self.fact = fact = [1] * (l + 1)
            self.inv = inv = [1] * (l + 1)
            for i in range(1, l + 1):
                fact[i] = fact[i - 1] * i % mod
            inv[l] = pow(fact[l], mod - 2, mod)
            for i in range(l - 1, -1, -1):
                inv[i] = inv[i + 1] * (i + 1) % mod
        
        def comb(self, n: int, r: int):
            return self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod if n >= r >= 0 else 0
        
        def perm(self, n: int, r: int):
            return self.fact[n] * self.inv[n - r] % self.mod if n >= r >= 0 else 0
    
    
    class PrefixSum2D:
        __slots__ = ["m", "n", "pre"]
        
        def __init__(self, mat: List[List[int]]):
            self.m = m = len(mat)
            self.n = n = len(mat[0])
            self.pre = pre = [[0] * (n + 1) for _ in range(m + 1)]
            for i, row in enumerate(mat):
                for j, v in enumerate(row):
                    pre[i + 1][j + 1] = pre[i][j + 1] + pre[i + 1][j] - pre[i][j] + v
        
        def find(self, r1: int, c1: int, r2: int, c2: int) -> int:
            """查询以(r1,c1)为左上角，(r2,c2)为右下角的矩形区间内所有值的和"""
            return self.pre[r2 + 1][c2 + 1] - self.pre[r2 + 1][c1] - self.pre[r1][c2 + 1] + self.pre[r1][c1]
    
    
    class Difference2D:
        __slots__ = ["m", "n", "diff"]
        
        def __init__(self, m, n):
            self.m = m
            self.n = n
            self.diff = [[0] * (n + 2) for _ in range(m + 2)]
        
        def add(self, r1: int, c1: int, r2: int, c2: int, delta: int):
            """下标从0开始，区间变化delta"""
            diff = self.diff
            diff[r1 + 1][c1 + 1] += delta
            diff[r1 + 1][c2 + 2] -= delta
            diff[r2 + 2][c1 + 1] -= delta
            diff[r2 + 2][c2 + 2] += delta
        
        def get(self) -> List[List[int]]:
            diff = self.diff
            for i in range(1, self.m + 1):
                for j in range(1, self.n + 1):
                    diff[i][j] += diff[i][j - 1] + diff[i - 1][j] - diff[i - 1][j - 1]
            diff = diff[1:-1]
            for i, row in enumerate(diff):
                diff[i] = row[1:-1]
            return diff
    
    
    class BinaryIndexedTree:
        __slots__ = ["n", "c"]
        
        def __init__(self, n: int):
            self.n = n
            self.c = [0] * (n + 1)
        
        def update(self, x: int, delta: int):
            while x <= self.n:
                self.c[x] += delta
                x += x & -x
        
        def query(self, x: int) -> int:
            s = 0
            while x > 0:
                s += self.c[x]
                x -= x & -x
            return s

if ConstType:
    RD = random.randint(10 ** 9, 2 * 10 ** 9)
    MOD1, MOD9, INF = 10 ** 9 + 7, 998244353, 10 ** 18
    Direction4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ->, <-, v, ^
    Direction8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # ->, <-, v, ^, ↘, ↙, ↗, ↖
    Y, N = "Yes", "No"


def solve():
    q = II()
    cnt = Counter()
    for _ in range(q):
        a = LII()
        if a[0] == 1:
            cnt[a[1]] += 1
        elif a[0] == 2:
            cnt[a[1]] -= 1
            if cnt[a[1]] == 0:
                del cnt[a[1]]
        else:
            print(len(cnt))


def C() -> None:
    for _ in range(1):
        solve()


if __name__ == '__main__':
    C()
