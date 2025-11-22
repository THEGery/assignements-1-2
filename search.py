#!usr/bin/env python

"""
.. moduleauthor:: Viktor Barath <viktor.barath7@gmail.com>

- ask the user for 2 strings
- Komma separated string of filenames (e.g. f1.txt, f2.txt)
- count NON-OVERLAPPING occurances of 2nd string
- not case sensitive
"""

files = input('Files: ')
needle = input('Needle: ')

# Separate the given string to two separate strings
separate_files = files.split(',')
files_list = separate_files
file_a = files_list[0].strip()
file_b = files_list[1].strip()

# Common function to look for non-overlapping occurrences
def count_non_overlapping(text, needle):
    """Compare non-overlapping occurrences."""
    occurrences = 0
    start = 0

    while True:
        index = text.find(needle, start)
        if index == -1:
            break
        occurrences += 1
        start = index + len(needle)

    return occurrences

# Opens files and reads content
with open(file_a, 'r') as f_a:
    text_a = f_a.read().lower()
with open(file_b, 'r') as f_b:
    text_b = f_b.read().lower()

# Count occurences in each file
occurrences_file_a = count_non_overlapping(text_a, needle)
occurrences_file_b = count_non_overlapping(text_b, needle)

total_occurrences = occurrences_file_a + occurrences_file_b


print(f'Occurrences: {total_occurrences}')
