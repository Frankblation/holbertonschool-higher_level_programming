#!/usr/bin/python3
"""def to write file"""


def write_file(filename="", text=""):
    with open(filename, mode='w', encoding='utf-8') as file:
        num_characters_written = file.write(text)
    return num_characters_written