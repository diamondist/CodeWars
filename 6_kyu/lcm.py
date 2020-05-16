from time import time
# from math import gcd

t1 = time()
a = [5262, 11111111, 255689]


from math import gcd
a = [7, 12, 3]   #will work for an int array of any length
lcm = a[0]
for i in a[1:]:
    lcm = lcm*i//gcd(lcm, i)
print(lcm)

# print(lcm(12, 7, 3))
t2 = time()
print(t2 - t1)
