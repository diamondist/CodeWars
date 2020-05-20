# Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string,
# the longest possible, containing distinct letters,
#
# each taken only once - coming from s1 or s2.
# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"
#
# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
#
# Test.describe("longest")
# Test.it("Basic tests")
# Test.assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
# Test.assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
# Test.assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")


def longest(s1, s2):
    result = ''
    for char in s1:
        if char not in result:
            result += char
    for char in s2:
        if char not in result:
            result += char
    return ''.join(sorted(result))

# better
#     def longest(s1, s2):
#     return ''.join(sorted(set(s1 + s2)))


a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
print(longest(a, b))
