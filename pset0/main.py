"""
 A program that asks the user to input a value for x, and a value for y.
 After the user inputs these values, the program calculates x^y and
 log2(x). Once these calculations are complete, it outputs them to
 the console.

 Author: James LaFarr
 Version: 12.2.22
 """

import math

x: int = int(input('Enter a number for x: '))
y: int = int(input('Enter a number for y: '))
print(f'x^y = {x**y}')
print(f'log2(x) = {math.log(x, 2)}')
