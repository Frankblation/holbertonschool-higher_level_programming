#!/usr/bin/python3
"""class my list def prints sorted list"""


class Mylist(list):

    def print_sorted(self):
        """prints list in ascending sorted order]
        """
        list = sorted(self)
        for item in list:
            print(item, end=' ')
        print()
