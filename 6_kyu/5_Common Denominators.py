# Common denominators
#
# You will have a list of rationals in the form
#
#  { {numer_1, denom_1} , ... {numer_n, denom_n} }
# or
#
#  [ [numer_1, denom_1] , ... [numer_n, denom_n] ]
# or
#
#  [ (numer_1, denom_1) , ... (numer_n, denom_n) ]
# where all numbers are positive ints.
#
# You have to produce a result in the form
#
#  (N_1, D) ... (N_n, D)
# or
#
#  [ [N_1, D] ... [N_n, D] ]
# or
#
#  [ (N_1', D) , ... (N_n, D) ]
# or
#
# {{N_1, D} ... {N_n, D}}
# or
#
# "(N_1, D) ... (N_n, D)"
# depending on the language (See Example tests)
#
# in which D is as small as possible and
#
#  N_1/D == numer_1/denom_1 ... N_n/D == numer_n,/denom_n.
# Example:
#
# convertFracs [(1, 2), (1, 3), (1, 4)] `shouldBe` [(6, 12), (4, 12),
# (3, 12)]
# Note:
# Due to the fact that first translations were written long ago - more
# than 4 years - these translations have only irreducible fractions.
# Newer translations have some reducible fractions. To be on the safe
# side it is better to do a bit more work by simplifying fractions even
# if they don't have to be.
#
# Note for Bash:
# input is a string, e.g "2,4,2,6,2,8"
#
# output is then "6 12 4 12 3 12"

# a = [[1, 2], [1, 3], [1, 4]]
# b = [[6, 12], [4, 12], [3, 12]]


# Test Results:
#  Log
# []
# None should equal []
#  Log
# [[1, 2], [1, 3], [1, 4]]
# None should equal [[6, 12], [4, 12], [3, 12]]
#  Log
# [[2, 7], [1, 3], [1, 12]]
# None should equal [[24, 84], [28, 84], [7, 84]]
#  Log
# [[69, 130], [87, 1310], [3, 4]]
# None should equal [[18078, 34060], [2262, 34060], [25545, 34060]]
#  Log
# [[77, 130], [84, 131], [3, 4]]
# None should equal [[20174, 34060], [21840, 34060], [25545, 34060]]
#  Log
# [[6, 13], [187, 1310], [31, 41]]
# None should equal [[322260, 698230], [99671, 698230], [527930,
# 698230]]
#  Log
# [[8, 15], [7, 111], [4, 25]]
# None should equal [[1480, 2775], [175, 2775], [444, 2775]]
#  Log
# [[1, 1], [3, 1], [4, 1], [5, 1]]
# None should equal [[1, 1], [3, 1], [4, 1], [5, 1]]
#  Log
# [[1, 100], [3, 1000], [1, 2500], [1, 20000]]
# None should equal [[200, 20000], [60, 20000], [8, 20000], [1, 20000]]
#  Log
# [[27115, 5262], [87546, 11111111], [43216, 255689]]
# None should equal [[77033412951888085, 14949283383840498],
# [117787497858828, 14949283383840498], [2526695441399712,
# 14949283383840498]]

from math import gcd


def convert_fracts(lst):
    if not lst:
        return lst
    dens = [item[1] for item in lst]
    lcm = dens[0]
    for i in dens[1:]:
        lcm = lcm * i // gcd(lcm, i)
    return [[lcm // i[1] * i[0], lcm] for i in lst]


a = [[27115, 5262], [87546, 11111111], [43216, 255689]]
print(convert_fracts(a))
