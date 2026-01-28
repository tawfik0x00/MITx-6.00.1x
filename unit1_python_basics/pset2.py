#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 20:13:42 2024

@author: horus
"""

# first we need to get the string
s = input('Enter an String: ')
count = 0

# wee need to loop through the string to count
# the number of substring 'bob in the string

for i in range(len(s) - 2): # to avoid last 3 chars and avoid out of bounds
    # from i to i + 3 = index 2 when i = 0
    # mean start at 0 through 3 chars and every time we add one to i
    # second 3 chars starting at s[i] to s[i + 2]
    if s[i:i+3] == 'bob':
        count += 1

print('number of times "bob" occurs is:', count)
