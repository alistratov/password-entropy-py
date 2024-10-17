import unittest
import random
import time

from data_password_entropy import password_entropy
from .decorators import loading_tests_enabled

"""
Load testing... 1000000 samples
v1
    Length 4: 1.229s 813528.1 ops/s
    Length 8: 2.210s 452428.2 ops/s
    Length 16: 4.185s 238949.3 ops/s
    Length 32: 8.288s 120662.3 ops/s
    
v2 - bitmask instead of set - DECREASED PERFORMANCE
    Length 4: 1.650s 605933.6 ops/s
    Length 8: 2.726s 366818.1 ops/s
    Length 16: 4.881s 204878.5 ops/s
    Length 32: 9.292s 107623.5 ops/s

v3 - list instead of set - OK
    Length 4: 1.340s 746299.0 ops/s
    Length 8: 2.261s 442205.1 ops/s
    Length 16: 4.097s 244053.9 ops/s
    Length 32: 7.928s 126138.0 ops/s
    
v4 - local vars - NO IMPROVEMENT
    Length 4: 1.357s 736931.8 ops/s
    Length 8: 2.230s 448340.2 ops/s
    Length 16: 4.080s 245108.5 ops/s
    Length 32: 7.842s 127513.9 ops/s

v5 - CharClasses singleton - DECREASED PERFORMANCE
    Length 4: 1.487s 672282.4 ops/s
    Length 8: 2.405s 415788.6 ops/s
    Length 16: 4.289s 233171.8 ops/s
    Length 32: 8.131s 122981.8 ops/s

v6 - W/out enumerate - OK
    Length 4: 1.231s 812498.4 ops/s
    Length 8: 2.107s 474637.8 ops/s
    Length 16: 3.990s 250648.0 ops/s
    Length 32: 7.624s 131157.2 ops/s
"""


class LiveRandomPasswords(unittest.TestCase):
    @loading_tests_enabled
    def test_random(self):
        PASSES = 1000
        LENGTHS = (4, 8, 16, 32)
        SAMPLES = 1000

        print(f'Load testing... {PASSES * SAMPLES} samples')
        for n in LENGTHS:
            passwords = []
            # Generate random passwords of length n
            # Char classes: lowercase, uppercase, digits, punctuation
            for _ in range(SAMPLES):
                p = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                                           '0123456789!@#$%^&*()_+-=/.,', k=n))
                passwords.append(p)

            # print(f'Length {n}: {passwords}')

            t1 = time.perf_counter()

            for _p in range(PASSES):
                for p in passwords:
                    _ = password_entropy(p)


            t2 = time.perf_counter()
            print(f'Length {n}: {t2 - t1:.3f}s {PASSES * SAMPLES / (t2 - t1):.1f} ops/s')
