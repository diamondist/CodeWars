# Given a positive number n > 1 find the prime factor decomposition of
# n. The result will be a string with the following form :
#
#  "(p1**n1)(p2**n2)...(pk**nk)"
# with the p(i) in increasing order and n(i) empty if n(i) is 1.
#                                    10   5    14   11
# Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
#
# test.assert_equals(primeFactors(7775460), "(2**2)(3**3)(5)(7)(11**2)(17)")
# 933555431


# Time: 863ms Passed: 0 Failed: 8 Exit Code: 1
# Test Results:
#  Log
# 7775460
# None should equal '(2**2)(3**3)(5)(7)(11**2)(17)'
#  Log
# 7919
# None should equal '(7919)'
#  Log
# 18195729
# None should equal '(3)(17**2)(31)(677)'
#  Log
# 933555431
# None should equal '(7537)(123863)'
#  Log
# 342217392
# None should equal '(2**4)(3)(11)(43)(15073)'
#  Log
# 35791357
# None should equal '(7)(5113051)'
#  Log
# 782611830
# None should equal '(2)(3**2)(5)(7**2)(11)(13)(17)(73)'
#  Log
# 775878912
# None should equal '(2**8)(3**4)(17)(31)(71)'
import time
from math import sqrt

def next_prime(prime):
    found = False
    while not found:
        prime += 1
        if (prime > 10):
            if (prime % 2 == 0) or (prime % 10 == 5):
                continue
        ceiling = int(sqrt(prime)) + 1
        for i in primes:
            if i > ceiling:
                break
            found = True
            if prime % i == 0:
                found = False
                break
    return prime


def primeFactors(n):
    global primes
    result = []
    while n > 1 or prime < sqrt(n):
        prime = primes[-1]
        while n % prime == 0:
            result.append(prime)
            n //= prime
        primes.append(next_prime(prime))
    res_str = ''
    for i in result:
        if f'({i}**{result.count(i)})' not in res_str:
            res_str += f'({i}**{result.count(i)})' if result.count(i) > 1 else f'({i})'
    return res_str

# test_list = [7775460, 7919, 18195729, 933555431, 342217392, 35791357, 782611830, 775878912]
# test_list = [56, 567, 2398]
# test_list = [933555431]     #5.77  #0.56  #0.22 #0.16  #0.14
# test_list = [7775460]           #4-05
test_list = [35791357]      #77   #25  #15



result_list = []
for i in test_list:
    result_string = ''
    primes = [2]
    t1 = time.time()
    result_string = primeFactors(i)
    t2 = time.time()
    timing = (t2 - t1)
    result_list.append((result_string, timing))

print(result_list)