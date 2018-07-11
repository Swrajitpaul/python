# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 12:54:30 2018

@author: swrajit
"""

x = -21474836480
bol = False
        
if x < 0:
    bol = True
    x = x * (-1)

st = str(x)
if int(st) > pow(2, 32):
    print(0)
if bol:
    st += '-'

st = st[::-1]

if st[0] == 0:
    st = st[1:]
    


print( int(st))
        