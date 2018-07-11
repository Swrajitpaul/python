# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:53:59 2018

@author: swrajit
"""

from random import randint
player = input('rock (r), paper(p), scissors(s)? ')
print(player, 'vs')

r = randint(1,2)
print(r)

if r ==1:
    computer = 'r'
    
elif r ==2:
    computer = 'p'
    
else:
    computer = 's'
    
print(computer)