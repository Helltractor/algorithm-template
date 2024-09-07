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


def CF593B():
    n = II()
    x1, x2 = MII()
    tmp = []
    for _ in range(n):
        k, b = MII()
        tmp.append((k * x1 + b, k * x2 + b))
    tmp.sort()
    for i in range(1, n):
        if tmp[i][1] < tmp[i - 1][1]:
            print(Y)
            return
    print(N)


if __name__ == '__main__':
    CF593B()
