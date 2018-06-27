# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 19:22:29 2018

@author: swrajit
"""

balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate / 12.0

b = balance
lowPay = 0

while True:
    b = balance
    for i in range(12):
        b -= lowPay
        b  = b + (b*monthlyInterestRate)
    if b > 0:
        lowPay += 10
    if b <= 0:
        break
print('Lowest Payment: ' + str(lowPay))