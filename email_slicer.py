#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Mario Burgos
# Tutorial: https://github.com/tomitokko/20-python-projects
# Youtube: https://youtu.be/pdy3nh1tn6I
# Created Date: Mon Sep 12 2022
# version ='1.0'
#
# collect the email address from user
# split the address using the '@'
# save first part as username, and second/third parts as domain '.' top-level-domain
#
# user @ domain . tld


def main():
    print("Welcome to the email slicer.\n")

    email_address = input(" Enter your email address: ")
    username, domain, tld = split_parts(email_address)
    display_parts(username, domain, tld)


def split_parts(email_address):
    username, domain = email_address.split("@")
    domain, tld = domain.split(".")

    return username, domain, tld

def display_parts(username, domain, tld):
    print(f"""
 Username: {username}
 Domain: {domain}
 TLD: {tld}
    """)


main()
