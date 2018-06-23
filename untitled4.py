# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:40:57 2018

@author: swrajit
"""

long =''
temp =''
var = ''
for i in range(len(s)):
    if (s[i] >= var):
        if var not in temp:
            temp += var
        temp += s[i]
    else :
        if len(temp) > len(long):
            long = temp
        temp = ''
    var = s[i]
    if len(temp) > len(long):
            long = temp
print('Longest substring in alphabetical order is: '+ long)