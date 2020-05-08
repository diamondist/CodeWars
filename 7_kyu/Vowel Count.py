# Return the number (count) of vowels in the given string.
#
# We will consider a, e, i, o, and u as vowels for this Kata.
#
# The input string will only consist of lower case letters and/or spaces.
#
# test.assert_equals(getCount("abracadabra"), 5)


def get_count(input_str):
    return sum(i in 'aeiou' for i in input_str)


print(get_count("abracadabra"))
