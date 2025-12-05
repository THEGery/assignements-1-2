#!/usr/bin/env python3

"""..modulauthor:: Viktor Barath viktor.barath7@gmail.com"""

interest_rate = float(input('Enter the fixed interest rate in percent: '))
investment_amount = float(input('Enter the amount of money you want to invest: '))
years_invested = float(input('Enter the number of years the money will be invested: '))


decimal_rate = interest_rate / 100


def calc_interest_earned(amount, rate, years):
    """ earned interest calculation I=P*r*t """
    interest = amount * (1 + rate ) ** years - amount
    return interest

earned_interest = calc_interest_earned(investment_amount, decimal_rate, years_invested)

print(f'The earned interest is {earned_interest:.2f}.')

def calc_future_value(amount, rate, years):
    """calculate terminal value FV=PV*(1+r)^n """
    fv_value = amount * (1 + rate) ** years
    return fv_value

future_value = calc_future_value(investment_amount, decimal_rate, years_invested)

print(f'The terminal value amounts to {future_value:.2f}.')