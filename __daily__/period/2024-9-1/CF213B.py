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
    from math import ceil, floor, sqrt, pi, factorial, gcd, lcm, log, log10, log2, inf
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

if ConstType:
    MOD1, MOD9 = 10 ** 9 + 7, 998244353
    RD = random.randint(MOD1, MOD1 << 1)
    Direction4 = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # ->, <-, v, ^
    Direction8 = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]  # ->, <-, v, ^, ↘, ↙, ↗, ↖
    Y, N = "Yes", "No"
    A, B = "Alice", "Bob"


def CF213B():
    n = II()
    a = LII()
    c = Math().comb
    
    @lru_cache(None)
    def dfs(i, j):
        if j == 9:
            if i < a[9]:
                return 0
            return 1
        res = 0
        for k in range(a[j], i + 1):
            res = (res + c(i - (j == 0), k) * dfs(i - k, j + 1)) % MOD1
        return res
    ans = 0
    for i in range(1, n + 1):
        ans = (ans + dfs(i, 0)) % MOD1
    print(ans % MOD1)
    
def CF213B_dp():
    n = II()
    a = LII()
    c = Math().comb
    f = [0] * (n + 1)
    for i in range(a[9], n + 1):
        f[i] = 1
    for j in range(8, -1, -1):
        for i in range(n, -1, -1):
            res = 0
            for k in range(a[j], i + 1):
                res = (res + f[i - k] * c(i - (j == 0), k)) % MOD1
            f[i] = res
    ans = 0
    for i in range(sum(a), n + 1):
        ans = (ans + f[i]) % MOD1
    print(ans % MOD1)
    
if __name__ == '__main__':
    #CF213B()
    CF213B_dp()
    