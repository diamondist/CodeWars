# Your job is to write a function which increments a string, to create a
# new string.
#
# If the string already ends with a number, the number should be
# incremented by 1.
# If the string does not end with a number. the number 1 should be
# appended to the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should
# be considered.
#
# Test.assert_equals(increment_string("foo"), "foo1")
# Test.assert_equals(increment_string("foobar001"), "foobar002")
# Test.assert_equals(increment_string("foobar1"), "foobar2")
# Test.assert_equals(increment_string("foobar00"), "foobar01")
# Test.assert_equals(increment_string("foobar99"), "foobar100")
# Test.assert_equals(increment_string("foobar099"), "foobar100")
# Test.assert_equals(increment_string(""), "1")


def increment_string(strng):
    number = ''
    if not strng:
        strng = '1'
    elif not strng[-1].isdigit():
        strng = strng + '1'
    else:
        i = -1
        number = ''
        while abs(i) <= len(strng) and strng[i].isdigit():
            number = strng[i] + number
            i -= 1
        strng = (strng[:-len(number)]
                 + ('0' * (len(number) - len(str(int(number) + 1))))
                 + str(int(number) + 1))
    return strng


print(increment_string("foo") == "foo1")
print(increment_string("foobar001") == "foobar002")
print(increment_string("foobar1") == "foobar2")
print(increment_string("foobar00") == "foobar01")
print(increment_string("foobar99") == "foobar100")
print(increment_string("foobar099") == "foobar100")
print(increment_string("foobar089") == "foobar090")
print(increment_string("") == "1")
increment_string('1')