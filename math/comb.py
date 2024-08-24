# _*_ coding: utf-8 _*_
# @File : comb.py
# @Time : 2024/4/22 10:40
# @Author : Helltractor
# @Description : Combination number

# mod = pow(10, 9) + 7
# l = 3 * pow(10, 5) + 5
# fac = [1] * (l + 1)
# inv = [1] * (l + 1)
# for i in range(1, l + 1):
#     fac[i] = fac[i - 1] * i % mod
# inv[l] = pow(fac[l], mod - 2, mod)
# for i in range(l - 1, -1, -1):
#     inv[i] = inv[i + 1] * (i + 1) % mod
# def comb(n, r):
#     return fac[n] * inv[r] % mod * inv[n - r] % mod if n >= r >= 0 else 0

class Comb:
    __slots__ = ["mod", "l", "fact", "inv"]
    
    def __init__(self):
        self.mod = mod = pow(10, 9) + 7
        self.l = l = 3 * pow(10, 5) + 5
        self.fact = fact = [1] * (l + 1)
        self.inv = inv = [1] * (l + 1)
        for i in range(1, l + 1):
            fact[i] = fact[i - 1] * i % mod
        inv[l] = pow(fact[l], mod - 2, mod)
        for i in range(l - 1, -1, -1):
            inv[i] = inv[i + 1] * (i + 1) % mod

    def comb(self, n, r):
        return self.fact[n] * self.inv[r] % self.mod * self.inv[n - r] % self.mod if n >= r >= 0 else 0
    