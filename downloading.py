#!usr/bin/env python

"""
.. moduleauthor:: Viktor Barath <viktor.barath7@gmail.com>
"""

import requests

def weekend_temp_from_webpage(url):
    """Get html data from url."""
    # Get data from URL
    # Assigne text without whitespaces
    get_web_page = requests.get(url)
    text = get_web_page.text.strip()
    # Split each line into string in the list called lines
    lines = text.splitlines()

    weekend_temp = []

    # Take each element in the lines list
    for line in lines:
        # Split elements to parts at whitespaces
        parts = line.split()
        day = parts[0]
        temp = int(parts[-1])
        if day in ('Saturday:', 'Sunday:'):
            weekend_temp.append(temp)

    return weekend_temp


def calculate_weekend_avg():
    """Calculate avarage temperature for the weekend."""
    weekend_temp = weekend_temp_from_webpage("https://study.find-santa.eu/data/py/fc.txt")
    weekend_sum = weekend_temp[0] + weekend_temp[1]
    avg_temp = weekend_sum / 2
    return avg_temp

def activity_suggestion():
    """Compare weekend avarage temp and suggest activity accordingly"""
    weekend_avg = calculate_weekend_avg()
    if weekend_avg > 25:
        suggestion = 'swimming'
    elif weekend_avg < 25:
        suggestion = 'hiking'
    elif weekend_avg < 12:
        suggestion = 'watching movies'
    elif weekend_avg < 5:
        suggestion = 'relaxing in the local hot springs'
    elif weekend_avg < -5:
        suggestion = 'skiing'

    print(f'Next weekend, {suggestion} would be a good activity.')

activity_suggestion()