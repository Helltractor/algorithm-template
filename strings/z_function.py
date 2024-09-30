#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2024/9/29 上午12:16

def z_function(t: str) -> list:
    z = [0] * len(t)
    l = r = 0
    for i in range(1, len(t)):
        if i <= r:
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < len(t) and t[z[i]] == t[i + z[i]]:
            l, r = i, i + z[i]
            z[i] += 1
    return z
