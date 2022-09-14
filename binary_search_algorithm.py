#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Mon Sep 12 2022
# version ='1.0'


# Get list (to search) and target to look for
# Calculate (of list): middle, start, end, steps (taken so far)
# Recurse/loop through list, increment step count
#   Each loop: 
# Once found, return element/value


def binary_search(list, target):
    start = steps = 0
    end = len(list)

    while(start < end):
        middle = (start + end) // 2
        print(f'Step: {steps} : {list[start:end+1]}')

        steps +=1

        if target == list[middle]:
            return middle
        elif target < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1


def get_input():
    list = input("List to use: ")
    list = list.split()
    target = input("Search target: ")

    return list, target


def main():
    list, target = get_input()
    binary_search(list, target)


main()
