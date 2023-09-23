#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
exe = 0
if number < 0:
    number *= -1
    exe = 1
last_digit = abs(number) % 10
if exe == 1:
    number *= -1
    last_digit *= -1
print(f'Last digit of {number} is {last_digit} and is', end=' ')
if last_digit > 5:
    print('greater than 5')
elif last_digit == 0:
    print('0')
else:
    print('less than 6 and not 0')
