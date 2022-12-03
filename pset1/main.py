"""
Assignment 1 for MIT's course Introduction to Computer Science and Programming with Python

Author: James LaFarr
Version: 12.2.22
"""

import math


def p1():
    annual_salary: float = float(input('What is your annual salary: '))
    percent_saved: float = float(input('What percent of your salary would you like to save: '))
    total_cost: float = float(input('What is the cost of your dream home: '))

    dp = total_cost * .25
    curr_savings = 0.
    annual_return = .04
    monthly_savings = (annual_salary * percent_saved) / 12

    months_counter = 0

    while curr_savings < dp:
        curr_savings += monthly_savings + (curr_savings * annual_return / 12)
        months_counter += 1

    print(f'It will take you {months_counter} months to save the needed money.')


def p2():
    annual_salary: float = float(input('What is your annual salary: '))
    percent_saved: float = float(input('What percent of your salary would you like to save: '))
    total_cost: float = float(input('What is the cost of your dream home: '))
    semi_raise: float = float(input('What is your semi-annual raise: '))

    dp: float = total_cost * .25
    curr_savings: float = 0.
    annual_return: float = .04
    monthly_savings: float = (annual_salary * percent_saved) / 12

    months_counter = 0

    while curr_savings < dp:
        curr_savings += ((annual_salary * percent_saved) / 12) + (curr_savings * annual_return / 12)
        months_counter += 1
        annual_salary *= (semi_raise + 1) if months_counter % 6 == 0 else 1

    print(f'It will take you {months_counter} months to save the needed money.')


def get_guess(lo: int, hi: int) -> int:
    return (lo + hi) // 2


def p3():
    ann_salary: float = float(input('What is your annual salary: '))
    mutable_salary = ann_salary

    semi_raise: float = .07
    ann_return: float = .04
    cost: float = 1000000.
    dp: float = cost * .25
    curr_savings: float = 0.
    epsilon: float = 100.

    if ann_salary * 3 < dp:
        print('You cannot pay for the downpayment in 3 years.')
        return float('inf')

    best_one = None
    best_diff = float('inf')
    low = 0
    high = 10000
    iterations = 0

    while iterations < math.log(10000, 2):
        mutable_salary = ann_salary
        iterations += 1
        guess = get_guess(low, high)
        curr_savings = 0
        for _ in range(1, 37):
            curr_savings += (curr_savings * ann_return / 12) + ((guess / 10000.) * mutable_salary / 12)
            if _ % 6 == 0:
                mutable_salary += mutable_salary * semi_raise
        if abs(dp - curr_savings) < best_diff:
            best_diff = abs(dp - curr_savings)
            best_one = guess
        if (dp - curr_savings) < 0:
            high = guess + 1
        else:
            low = guess - 1
    return best_one / 10000
