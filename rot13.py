#!usr/bin/env python

"""
.. moduleauthor:: Viktor Barath <viktor.barath7@gmail.com>
"""
input_file = input('File to decode: ')

def read_file(file):
    """Read file in and convert it all uppercase."""
    message = ''
    with open(file) as f:
        message += f.read()

    return message


def rot13(message):
    """Encrypt, decrypt input text."""
    offset = 13
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    translated_message = ''

    for char in message.upper():
        if not char.isalpha():
            translated_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            translated_message += alphabet[new_index]

    return translated_message

message = read_file(input_file)

print(f'Translated message:\n{rot13(message)}')