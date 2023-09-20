#!/usr/bin/python3
"""print a square out of hashtags
"""


def print_square(size):
    """
    Args:
        size (int): size of the square, it must be an integer

    Raises:
        TypeError: size must be an integer
        ValueError: size must be great then, not negative
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print("#" * size)
