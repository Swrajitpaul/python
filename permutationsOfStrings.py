# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 00:18:26 2018

@author: swrajit
"""

def a(b, c):
    if len(b) == len(c):
        print(b)
        return
    else:
        for char in c:
            if char not in b:
                b.append(char)
                a(b,c)
                #b.remove(char)
 
b = []               
c =['A','B', 'C', 'D']
a(b,c)