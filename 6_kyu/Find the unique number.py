# There is an array with some numbers. All numbers are equal except for
# one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.


def find_uniq(arr):
    multiple = None
    for i in arr:
        if arr.count(i) > 1:
            multiple = i
            break
    return [i for i in set(arr) if i != multiple][0]


print(find_uniq([1, 1, 1, 2, 1, 1]))
