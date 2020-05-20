# You have an array of numbers.
# Your task is to sort ascending odd numbers but even numbers must be on
# their places.
#
# Zero isn't an odd number and you don't need to move it. If you have an
# empty array, you need to return it.
#
# Example
#
# sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]


def sort_array(source_array):
    evens_array = [(i, ev) for i, ev in enumerate(source_array) if ev % 2 == 0]
    odds_array = sorted([i for i in source_array if i % 2 != 0])
    for el in evens_array:
        odds_array.insert(el[0], el[1])
    return odds_array


sort_array([5, 3, 2, 8, 1, 4])
