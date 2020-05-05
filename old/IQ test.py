# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which
# one of the given numbers differs from the others. Bob observed that one number usually differs
# from the others in evenness. Help Bob — to check his answers, he needs a program that among
# the given numbers finds one that is different in evenness, and return a position of this number.
#
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes
# of the elements start from 1 (not 0)
# Test.assert_equals(iq_test("2 4 7 8 10"),3)
# Test.assert_equals(iq_test("1 2 2"), 1)

test = "47 21 14 29 25 37 11 15 21 7 47 49 35 35 41 51 45 25 25 13 11 33 9 37 1 27 37 47 11 51 13 49 13 33 37 49 37 21 13 9 19 29"
test_list = test.split()
print(test_list)
even_counter = 0
odd_counter = 0
for el in test_list:
    if int(el) % 2 == 0:
        even_counter += 1
    else:
        odd_counter += 1
if even_counter == 1:
    for el in test_list:
        if int(el) % 2 == 0:
            result = test_list.index(el) +1
elif odd_counter == 1:
    for el in test_list:
        if int(el) % 2 != 0:
            result = test_list.index(el) + 1
print(even_counter, odd_counter)
print(result)



def iq_test(numbers):
    e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1



