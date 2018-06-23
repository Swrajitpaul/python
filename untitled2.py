# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:40:09 2018

@author: swrajit
"""

var = 0
for char in s:
    x = char
    if x == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        var += 1
print('Number of vowels: ' + str(var))