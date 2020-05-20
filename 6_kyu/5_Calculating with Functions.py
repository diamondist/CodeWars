# This time we want to write calculations using functions and get the
# results. Let's have a look at some examples:
#
# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:
#
# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical
# operations: plus, minus, times, dividedBy (divided_by in Ruby and
# Python)
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner
# function represents the right operand
# Divison should be integer division. For example, this should return 2,
# not 2.666666...:
# eight(divided_by(three()))
#
# Test.assert_equals(seven(times(five())), 35)
# Test.assert_equals(four(plus(nine())), 13)
# Test.assert_equals(eight(minus(three())), 5)
# Test.assert_equals(six(divided_by(two())), 3)


def zero(*args):
    if args:
        if args[0][0] == 'times':
            return 0 * args[0][1]
        if args[0][0] == 'divided_by':
            return 0 // args[0][1]
        if args[0][0] == 'plus':
            return 0 + args[0][1]
        if args[0][0] == 'minus':
            return 0 - args[0][1]
    else:
        return 0


def one(*args):
    if args:
        if args[0][0] == 'times':
            return 1 * args[0][1]
        if args[0][0] == 'divided_by':
            return 1 // args[0][1]
        if args[0][0] == 'plus':
            return 1 + args[0][1]
        if args[0][0] == 'minus':
            return 1 - args[0][1]
    else:
        return 1


def two(*args):
    if args:
        if args[0][0] == 'times':
            return 2 * args[0][1]
        if args[0][0] == 'divided_by':
            return 2 // args[0][1]
        if args[0][0] == 'plus':
            return 2 + args[0][1]
        if args[0][0] == 'minus':
            return 2 - args[0][1]
    else:
        return 2


def three(*args):
    if args:
        if args[0][0] == 'times':
            return 3 * args[0][1]
        if args[0][0] == 'divided_by':
            return 3 // args[0][1]
        if args[0][0] == 'plus':
            return 3 + args[0][1]
        if args[0][0] == 'minus':
            return 3 - args[0][1]
    else:
        return 3


def four(*args):
    if args:
        if args[0][0] == 'times':
            return 4 * args[0][1]
        if args[0][0] == 'divided_by':
            return 4 // args[0][1]
        if args[0][0] == 'plus':
            return 4 + args[0][1]
        if args[0][0] == 'minus':
            return 4 - args[0][1]
    else:
        return 4


def five(*args):
    if args:
        if args[0][0] == 'times':
            return 5 * args[0][1]
        if args[0][0] == 'divided_by':
            return 5 // args[0][1]
        if args[0][0] == 'plus':
            return 5 + args[0][1]
        if args[0][0] == 'minus':
            return 5 - args[0][1]
    else:
        return 5


def six(*args):
    if args:
        if args[0][0] == 'times':
            return 6 * args[0][1]
        if args[0][0] == 'divided_by':
            return 6 // args[0][1]
        if args[0][0] == 'plus':
            return 6 + args[0][1]
        if args[0][0] == 'minus':
            return 6 - args[0][1]
    else:
        return 6


def seven(*args):
    if args:
        if args[0][0] == 'times':
            return 7 * args[0][1]
        if args[0][0] == 'divided_by':
            return 7 // args[0][1]
        if args[0][0] == 'plus':
            return 7 + args[0][1]
        if args[0][0] == 'minus':
            return 7 - args[0][1]
    else:
        return 7


def eight(*args):
    if args:
        if args[0][0] == 'times':
            return 8 * args[0][1]
        if args[0][0] == 'divided_by':
            return 8 // args[0][1]
        if args[0][0] == 'plus':
            return 8 + args[0][1]
        if args[0][0] == 'minus':
            return 8 - args[0][1]
    else:
        return 8


def nine(*args):
    if args:
        if args[0][0] == 'times':
            return 9 * args[0][1]
        if args[0][0] == 'divided_by':
            return 9 // args[0][1]
        if args[0][0] == 'plus':
            return 9 + args[0][1]
        if args[0][0] == 'minus':
            return 9 - args[0][1]
    else:
        return 9


def plus(arg2):
    return 'plus', arg2


def minus(arg2):
    return 'minus', arg2


def times(arg2):
    return 'times', arg2


def divided_by(arg2):
    return 'divided_by', arg2


print(two(minus(zero())))

# TODO: review with lambda
# id_ = lambda x: x
# number = lambda x: lambda f=id_: f(x)
# zero, one, two, three, four, five, six, seven, eight, nine = map(number, range(10))
# plus = lambda x: lambda y: y + x
# minus = lambda x: lambda y: y - x
# times = lambda x: lambda y: y * x
# divided_by = lambda x: lambda y: y / x

# TODO: review with eval
# def zero(arg=""):  return eval("0" + arg)
# def one(arg=""):   return eval("1" + arg)
# def two(arg=""):   return eval("2" + arg)
# def three(arg=""): return eval("3" + arg)
# def four(arg=""):  return eval("4" + arg)
# def five(arg=""):  return eval("5" + arg)
# def six(arg=""):   return eval("6" + arg)
# def seven(arg=""): return eval("7" + arg)
# def eight(arg=""): return eval("8" + arg)
# def nine(arg=""):  return eval("9" + arg)
#
# def plus(n):       return "+%s" % n
# def minus(n):      return "-%s" % n
# def times(n):      return "*%s" % n
# def divided_by(n): return "/%s" % n
