# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:41:05 2018

@author: swrajit
"""

monthlyInterest= annualInterestRate / 12.0
for i in range(1,13):
    monthlyPayment = monthlyPaymentRate * balance
    balance = balance - monthlyPayment
    balance = balance + monthlyInterest * balance
    #print('Month ' + str(i) + ' Remaining balance: ' + str(balance))
print('Remaining balance: ' + str(round(balance, 2)))