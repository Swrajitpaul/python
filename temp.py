# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

max = 0
for i in range(10):
    temp = int(input('Enter an integer'))
    if(temp % 2 == 1):
        if(max <= temp):
            max = temp
            