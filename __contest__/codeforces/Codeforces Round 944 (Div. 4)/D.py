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
 
def cf_D():
    for _ in range(II()):
        s = I()
        cnt0 = sum(len(x) > 0 for x in s.split('0'))
        cnt1 = sum(len(x) > 0 for x in s.split('1'))
        ans = cnt0 + cnt1
        if len(s) > 1:
            for i in range(len(s) - 1):
                if s[i] != s[i + 1] and s[i] == '0':
                    ans -= 1
                    break
        print(ans)


    return 
 
def main():
    cf_D()
    return 
 
if __name__ == '__main__':
    main()