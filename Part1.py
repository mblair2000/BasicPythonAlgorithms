'''
This class contains two methods, one to find the power of a number
and another to find all prime integers within a range

Created on Feb 9, 2021
@author: mblair2000
'''

import math


'''
This method finds a number raised to a power using a loop
'''
def powr(x, n):
    power = 1
    for i in range(n):
        power = power * x
    return power


print(powr(2, 2))
print(powr(3, 2))
print(powr(3, 3))


'''
This method finds all the prime numbers within a range
'''
def prime(low, high):
    primeNums = []
    for i in range(low, high + 1):
        bool1 = True
        for x in range(2, i):
            if (i % x) == 0:
                bool1 = False
                break
        if (bool1):
            if (i != 1 and i != 0):
                primeNums.append(i)
    return primeNums


print("\n",prime(0, 19))
print(prime(100, 200))