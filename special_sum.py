#!usr/bin/env python

"""
.. moduleauthor:: Viktor Barath <viktor.barath7@gmail.com>
"""

divisor = 7

print(f'Denominator: {divisor}')

limit = int(input('Upper limit: '))

divisible = []
for i in range(1, (limit + 1)):
    if i % divisor == 0:
        divisible.append(i)
        result = sum(divisible)

print(result)
