# Implement the function unique_in_order which takes as argument a sequence and returns a list of items
# without any elements with the same value next to each other and preserving the original order of
# elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]



iterable = 'A'
lst = [el for el in iterable]
print(lst)
result = []
for i in range(len(lst)):
    if i:
        if lst[i] != lst[i - 1]:
            result.append(lst[i])
    else:
        result.append(lst[i])
print(result)

# best:
def unique_in_order(iterable):
    result = list(iterable[:1])
    for char in iterable:
        if char != result[-1]:
            result.append(char)
    return result