#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Wed Sep 14 2022
# version ='1.0'

# Get financial input from user: pricipal; APR; years
# Output monthly payment for user


def get_input():
    principal = float(input(" Loan amount: "))
    apr = float(input(" Annual interest rage (%): "))
    years = int(input(" Term of loan (years): "))

    return principal, apr, years

def monthly_payment(total, apr, term):
    monthly_interest_rate = apr / 1200
    months = term * 12
    monthly_interest = total * monthly_interest_rate
    # calculate monthly payment
    monthly_payment = total * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-months))

    return monthly_interest, monthly_payment

def main():
    print(" Monthly loan payment calculator\n")

    principal, apr, years = get_input()
    interest, payment = monthly_payment(principal, apr, years)

    print(f"""
 Monthly payment: ${payment:.2f}
 (Includes) monthly interst of: ${interest:.2f}
 """)


main()
