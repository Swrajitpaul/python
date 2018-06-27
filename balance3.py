# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:44:25 2018

@author: swrajit
"""


Balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate / 12.0

lower = Balance/12
higher = (Balance *(1 + monthlyInterestRate)** 12)/12.0

totalBalance = (Balance *(1 + monthlyInterestRate)** 12)
middle = ((lower + higher)/2)
leftBalance = totalBalance - middle*12

while not leftBalance == 0.0:
    if (leftBalance > 0.0):
        lower = middle 
    elif leftBalance < 0.0:
        higher = middle
    
print(middle)
    