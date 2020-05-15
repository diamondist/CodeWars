# There is an array of strings. All strings contains similar letters
# except one. Try to find it!
#
# find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ])
# => 'BbBb'
# find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ])
# => 'foo'
# Strings may contain spaces. Spaces is not significant, only non-spaces
# symbols matters. E.g. string that contains only spaces is like empty
# string.
#
# It’s guaranteed that array contains more than 3 strings.
#
# test.describe('should handle sample cases')
# (find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]),
# 'BbBb')
# (find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]),
# 'foo')
# (find_uniq([ '    ', 'a', '  ' ]), 'a')


def find_uniq(arr):
    if set(arr[0].lower()) != set(arr[1].lower()):
        result = arr[0] if set(arr[2].lower()) != set(arr[0]) else arr[1]
    else:
        for i in arr:
            if set(i.lower()) != set(arr[0].lower()):
                result = i
                break
    return result


print(find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]))
