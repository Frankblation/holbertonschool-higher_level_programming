#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list is None:
        return None
    if len(my_list) == 0:
        return None

    highest = float("-inf")

    for num in my_list:
        if num > highest:
            highest = num

    print("Max: {:d}".format(highest))
    return highest
