# _*_ coding: utf-8 _*_
# @File : primes.py
# @Time : 2024/8/2 下午2:56
# @Author : Helltractor

import time
import unittest

class Primes:
    
    @staticmethod
    def fool_primes(n):
        """暴力枚举"""
        primes = []
        for i in range(2, n):
            if all(i % j != 0 for j in range(2, i)):
                primes.append(i)
        return primes
    
    @staticmethod
    def primes_enumeration(n: int) -> int:
        """枚举"""
        def is_prime(n):
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True if n > 1 else False
        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes
    
    @staticmethod
    def primes_enumeration_plus(n: int) -> int:
        """枚举优化"""
        def is_prime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True if n > 1 else False
        primes = []
        for i in range(2, n):
            if is_prime(i):
                primes.append(i)
        return primes
    
    @staticmethod
    def primes_linear(n: int) -> int:
        """线性筛"""
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
            for p in primes:
                if i * p >= n: break
                is_prime[i * p] = False
                if i % p == 0: break
        primes.extend([n, n])   # 防止下标越界
        return primes
    
    @staticmethod
    def primes_ealich(n: int) -> int:
        """埃氏筛"""
        primes = []
        is_prime = [False] * 2 + [True] * (n - 2)
        for i in range(2, n):
            if is_prime[i]:
                primes.append(i)
                for j in range(i ** 2, n, i):
                    is_prime[j] = False
        primes.extend([n, n])   # 防止下标越界
        return primes


class MyTestCase(unittest.TestCase):
    
    n = pow(2, 16)
    
    def test_primes_linear(self):
        start_time = time.time()
        Primes.primes_linear(self.n)
        end_time = time.time()
        print('primes_linear:', end_time - start_time)
        return
    
    def test_primes_ealich(self):
        start_time = time.time()
        Primes.primes_ealich(self.n)
        end_time = time.time()
        print('primes_ealich:', end_time - start_time)
        return
    
    def test_primes_enumeration(self):
        start_time = time.time()
        Primes.primes_enumeration(self.n)
        end_time = time.time()
        print('primes_enumeration:', end_time - start_time)
        return
    
    def test_primes_enumeration_plus(self):
        start_time = time.time()
        Primes.primes_enumeration_plus(self.n)
        end_time = time.time()
        print('primes_enumeration_plus:', end_time - start_time)
        return


if __name__ == '__main__':
    unittest.main()
    