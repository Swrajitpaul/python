# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 16:08:26 2018

@author: swrajit
"""
import random

a = [['-'] * 3] * 3

won = False

print("who goes first....Player 1 or Player 2")

player = 0
while (player < 1 or player > 2 ):
    player = int(input("Enter player number \n"))

last = 0

while(not won):
    