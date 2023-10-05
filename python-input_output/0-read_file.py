#!/usr/bin/python3
"""def to readfile"""

def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as file:
        content = file.read()
        print(content)
