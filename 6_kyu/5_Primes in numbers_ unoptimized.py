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


def next_prime(prime):
    found = False
    while not found:
        prime += 1
        for i in range(2, prime):
            found = True
            if prime % i == 0:
                found = False
            if not found:
                break
    return prime


def primeFactors(n):
    result = []
    prime = 2
    while n > 1:
        while n % prime == 0:
            result.append(prime)
            n //= prime
        prime = next_prime(prime)
    res_str = ''
    for i in result:
        if f'({i}**{result.count(i)})' not in res_str:
            res_str += f'({i}**{result.count(i)})' if result.count(i) > 1 else f'({i})'
    return res_str


print(primeFactors(7775460))
