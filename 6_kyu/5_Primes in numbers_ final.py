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

# test_list = [7775460, 7919, 18195729, 933555431, 342217392, 35791357, 782611830, 775878912]
# test_list = [56, 567, 2398]
# test_list = [933555431]     #5.77  #0.56  #0.22 #0.16  #0.14       #0.04
# test_list = [7775460]           #4-05
# test_list = [35791357]      #77   #25  #15  #0.001

from math import sqrt


def primeFactors(n):
    result = []
    for i in range(2, int(sqrt(n))):
        while n % i == 0:
            result.append(i)
            n //= i
    if n > 1:
        result.append(n)
    res_str = ''
    for i in result:
        if f'({i}**{result.count(i)})' not in res_str:
            res_str += f'({i}**{result.count(i)})' if result.count(i) > 1 else f'({i})'
    return res_str
