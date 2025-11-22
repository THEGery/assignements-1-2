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

def avarage_closing_price():
    """Calculate avg closing price."""
    pass


print(collect_close_column_numbers('Download Data - STOCK_AT_XWBO_ANDR.csv'))
