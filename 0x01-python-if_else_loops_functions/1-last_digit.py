#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = abs(number)
last_digit = value % 10

if number < 0:
    last_digit = last_digit * (-1)

if last_digit > 5:
    print('Last digit of {} is {} and is greater'
          ' than 5'.format(number, last_digit))
elif last_digit == 0:
    print('Last digit of {} is {} and is '
          '0'.format(number, last_digit))
else:
    print('Last digit of {} is {} and is less '
          'than 6 and not 0'.format(number, last_digit))
