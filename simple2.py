# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:07:34 2018

@author: swrajit
"""

l = [[1]*3]*3
for i in range(3):
    for j in range(3):
        print(l[i][j], end ="")
    print(end="\n")