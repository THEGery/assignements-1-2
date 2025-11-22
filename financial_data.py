#!usr/bin/env python

"""
.. moduleauthor:: Viktor Barath <viktor.barath7@gmail.com>
"""

def collect_close_column_numbers(file):
    """Open file, read content, collect close column numbers stripped."""
    close_numbers = []
    with open(file, 'r') as file:
        for line in file:
            line.split()
            clean_line = line.replace('"', '')
            elements = clean_line.split(",")
            close_numbers.append(elements[4])
    return close_numbers[1:]

close_num_list = collect_close_column_numbers(
        'Download Data - STOCK_AT_XWBO_ANDR.csv')

def avg_closing_price():
    """Calculate avg closing price."""
    sum_closing_price = 0
    for price in close_num_list:
        sum_closing_price += float(price)
    avg_closing_price = sum_closing_price / len(close_num_list)

    return avg_closing_price


def check_last_price(last_price):
    avg_closing = avg_closing_price()
    if avg_closing < last_price:
        indicator = 'above' #last price was above
    elif avg_closing > last_price:
        indicator = 'below' #last price was below
    else:
        indicator = 'the same as'

    return indicator


last_price = float(close_num_list[-1])

print(f'The avargae closing price was {avg_closing_price():.2f}.')

print(f'The most recent closing price {avg_closing_price():.2f} was '
      f'{check_last_price(last_price)} the avarage.')
