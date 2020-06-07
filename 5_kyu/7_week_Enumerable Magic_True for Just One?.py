# Create a function called one that accepts two params:
#
# a sequence
# a function
# and returns true only if the function in the params returns true for
# exactly one (1) item in the sequence.
#
# Example
# one([1, 3, 5, 6, 99, 1, 3], bigger_than_ten) -> true
# one([1, 3, 5, 6, 99, 88, 3], bigger_than_ten) -> false
# one([1, 3, 5, 6, 5, 1, 3], bigger_than_ten) -> false


# @test.describe('Example Tests')
# def example_tests():
#     equals_9 = lambda x: x == 9
#     greater_than_9 = lambda x: x > 9
#     arr = (6, 7, 8, 9, 10, 11)
#
#     test.assert_equals(one(arr, equals_9), True)
#     test.assert_equals(one(arr, less_than_9), False)
#


def equals_9(x):
    return x == 9


def greater_than_9(x):
    return x > 9


def less_than_9(x):
    return x < 9


def one(sq, fun):
    return list(map(fun, sq)).count(True) == 1
