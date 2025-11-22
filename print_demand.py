#!usr/bin/env python

"""
..modulauther:: Viktor Barath <viktor.barath7@gmail.com>
"""

import requests
from bs4 import BeautifulSoup

url = 'https://study.find-santa.eu/data/py/r101.txt'
get_text = requests.get(url)
html_content = get_text.text

soup = BeautifulSoup(html_content, 'html.parser')
texts = soup.get_text()


print(data)