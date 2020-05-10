# An isogram is a word that has no repeating letters, consecutive or
# non-consecutive. Implement a function that determines whether a
# string that contains only letters is an isogram. Assume the empty
# string is an isogram. Ignore letter case.
#
# is_isogram("Dermatoglyphics" ) == true
# is_isogram("aba" ) == false
# is_isogram("moOse" ) == false # -- ignore letter case


def is_isogram(string):
    result = True
    for char in string:
        if string.lower().count(char) > 1:
            result = False
    return result


print(is_isogram("moOse"))


# much better
# def is_isogram(string):
#     return len(string) == len(set(string.lower()))
