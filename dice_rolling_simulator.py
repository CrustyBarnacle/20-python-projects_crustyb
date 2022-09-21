#!/usr/bin/env python3

""" -*- coding: utf-8 -*-
 Created By  : Mario Burgos
 Tutorial: https://github.com/tomitokko/20-python-projects
 Youtube: https://youtu.be/pdy3nh1tn6I
 Created Date: Tue Sep 20 2022
 version ='1.0'
"""

""" Placeholder for v2.0
import random


def roll_dice(sides):
    print(f'd{sides}: ')
    return random.randint(1,sides)


def main():
    print(f'Random result: {roll_dice()}')


main()

"""

import random

def roll_dice():

    dice_drawing = {
        1: (
            "-----",
            "|     |",
            "|  o  |",
            "|     |",
            "-------",
        ),
        2: (
            "-----",
            "| o   |",
            "|     |",
            "|   o |",
            "-------",
        ),
        3: (
            "-------",
            "| o   |",
            "|  o  |",
            "|   o |",
            "-------",
        ),
        4: (
            "-------",
            "| o o |",
            "|     |",
            "| o o |",
            "-------",
        ),
        5: (
            "-------",
            "| o o |",
            "|  o  |",
            "| o o |",
            "-------",
        ),
        6: (
            "-------",
            "| o o |",
            "| o o |",
            "| o o |",
            "-------",
        ),

    }

    roll = input("Roll the dice? (Yes/No) : ")

    while roll.lower() == "Yes". lower():
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("dice rolled: {} and {}". format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))
        
        roll = input("Roll again? (Yes/no): ")


roll_dice()
