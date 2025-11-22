#!usr/bin/env python

"""
.. moduleauthor:: Viktor Barath <viktor.barath7@gmail.com>
"""

integer = 63
print(f'Integer: {integer} =', end=' ')

factors = []

# If intiger divisible by 2 without remeinder, it's a factor
while integer % 2 == 0:
    factors.append(2)
    # Divide with smallest prime as many times as possible
    integer //= 2

# Change divisor to next smallest prime
divisor = 3
# Int cannot be 1 and larger than 3
while integer != 1 and divisor <= integer:
    if integer % divisor == 0:
        factors.append(divisor)
        # Divide with current prime as many times as possible
        integer //= divisor
    else:
        # Prime numbers are odd ecept 2
        # Adding 2 to divisor results always odd number
        # Because 3 + 2 = 5 -> 5 + 2 = 7 ...
        divisor += 2

# For-loop takes elements out of list
for i in range(len(factors)):
    # If i is not the last item
    if i < len(factors) - 1:
        print(f'{factors[i]} *', end=' ')
    else:
        print(factors[i])
