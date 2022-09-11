#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Fri Sep 10 2022
# version ='2.0'


# Calculation functions
def add(a, b):
    print(f" {a} + {b} = {a + b}\n")

def multiply(a, b):
    print(f" {a} x {b} = {a * b}\n")

def subtract(a, b):
    print(f" {a} - {b} = {a - b}\n")

def divide(a, b):
    try:
        print(f" {a} / {b} = {a // b}r{a % b}\n")
    except ZeroDivisionError as error:
        print(f"Error: {error}")


# Help - choices
def output_help():
    operation_choices = """
  A. Addition
  B. Subtraction
  C. Multiplication
  D. Division
  Q. Quit"""

    print(operation_choices)

# User Input
def get_choice():
    choice = "z" # Use do while and no need for initializing choice?
    while choice not in ['a','b','c','d','q']:
        output_help()
        choice = input(f"Operation to use: ").lower()

        if choice == "q":
            print("Quitting calculator...")
            quit()

    match choice:
        case "a":
            print("Addition")
        case "b":
            print("Subtraction")
        case "c":
            print("Multiplication")
        case "d":
            print("Division")

    return choice


def get_numbers():
    a = int(input(" First number: "))
    b = int(input(" Second number: "))

    return a, b


# Using chosen operation and numbers, output result

def get_result(operation, a, b):
    match operation.lower():
        case "a":
            add(a, b)
        case "b":
            subtract(a, b)
        case "c":
            multiply(a, b)
        case "d":
            divide(a, b)


# Get choice of operation, numbers, calculate and output result

while True:
    operation = get_choice()
    a, b = get_numbers()
    get_result(operation, a, b)
