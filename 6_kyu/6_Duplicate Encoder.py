# The goal of this exercise is to convert a string to a new string where
# each character in the new string is "(" if that character appears only
# once in the original string, or ")" if that character appears more
# than once in the original string. Ignore capitalization when
# determining if a character is a duplicate.
#
# Examples
# "din"      =>  "((("
# "recede"   =>  "()()()"
# "Success"  =>  ")())())"
# "(( @"     =>  "))(("


def duplicate_encode(word):
    low_word = word.lower()
    return ''.join(['(' if low_word.count(i) == 1 else ')' for i in low_word])


print(duplicate_encode('CodeWarrior'))
