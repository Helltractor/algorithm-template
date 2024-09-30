#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : daily/8/29 下午12:38
import time
import unittest

from mathmatics.prime.template import Primes


class MyTestCase(unittest.TestCase):
    n = 2 * pow(10, 5)
    
    def test_primes_linear(self):
        start_time = time.time()
        primes = Primes.primes_linear(self.n)
        print(len(primes), primes)
        end_time = time.time()
        print('primes_linear:', end_time - start_time)
            
    def test_primes_ealich(self):
        start_time = time.time()
        primes = Primes.primes_ealich(self.n)
        print(len(primes), primes)
        end_time = time.time()
        print('primes_ealich:', end_time - start_time)
            
    def test_primes_enumeration(self):
        start_time = time.time()
        Primes.primes_enumeration(self.n)
        end_time = time.time()
        print('primes_enumeration:', end_time - start_time)
            
    def test_primes_enumeration_plus(self):
        start_time = time.time()
        Primes.primes_enumeration_plus(self.n)
        end_time = time.time()
        print('primes_enumeration_plus:', end_time - start_time)
        