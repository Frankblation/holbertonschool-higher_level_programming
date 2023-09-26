#!/usr/bin/python3
"""class my list def prints sorted list"""


class Mylist(list):
    """ my sorted list

    Args:
        list (integers): numbers of list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """prints list in ascending sorted order]
        """
        sorted_list = sorted(self)
        print(sorted_list)
