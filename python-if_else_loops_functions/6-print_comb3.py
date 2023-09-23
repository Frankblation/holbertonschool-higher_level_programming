#!/usr/bin/python3

for tens_digit in range(0, 10):
    for ones_digit in range(tens_digit + 1, 10):
        if tens_digit != ones_digit:
            if tens_digit == 0 and ones_digit == 1:
                print("01", end='')
            else:
                print("{:02d}".format(tens_digit * 10 + ones_digit), end='\n')
            if tens_digit < 8 or ones_digit < 9:
                print(", ", end='')
