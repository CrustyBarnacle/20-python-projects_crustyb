#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Fri Sep  9 03:19 PM PDT 2022
# version ='1.0'

def replace_word():

    str = "Hi everyone, hi hi hi hi"
    word_to_replace = input("Word to replace: ")
    word_replacement = input("Replacement word: ")

    print(f'New string: {str.replace(word_to_replace, word_replacement)}')

replace_word()
