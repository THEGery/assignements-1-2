#!usr/bin/env python

"""
.. moduleauthor:: Viktor Barath <viktor.barath7@gmail.com>
"""

import requests

def get_data_from_webpage(url):
    """Fetch data from given webpage"""
    get_webpage = requests.get(url)
    text = get_webpage.text.strip()
    lines = text.splitlines()

    column_demand = []

    for line in lines:
        # Splits lines into elements, where whitespace is
        parts = line.split()
        # Assigne column demand only
        column_demand.append(parts [3])

    return column_demand

def calc_total_demand():
    """Sum numbers from demand"""
    demand_lines = get_data_from_webpage('https://study.find-santa.eu/data/py/r101.txt')
    total_demand = 0

    for demand in demand_lines:
        if not demand.isalpha():
            total_demand += float(demand)

    return total_demand

print(f'Total demand: {calc_total_demand()}')