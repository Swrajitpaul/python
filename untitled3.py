# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:40:33 2018

@author: swrajit
"""

total = 0
i = 0
for i in range(len(s)-2):
    if s[i:i+3] == 'bob':
        total += 1
print('Number of times bob occurs is: ' + str(total))