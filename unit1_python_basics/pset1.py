#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:07:21 2024

@author: horus
"""

# first we need the string to check
s = input('Enter a string: ')

# loop through string to count number of vowels
# initialize a counter
count = 0
for c in s:
    if c in 'aeoiu':
        count += 1

print('Number of vowels:', count)