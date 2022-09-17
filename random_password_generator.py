#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Sat Sep 17 2022
# version ='1.0'

# Request password length
# Generate password
# TODO: update to use secrets


import random
import string
#import secrets


characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password = []
    
    password_length = int(input(" Length of password: "))

    random.shuffle(characters)

    for i in range(password_length):
        password.append(random.choice(characters))
    
    password = "".join(password)
    
    return password


def main():
    password = generate_password()
    print(f"New random password: {password}")


main()
