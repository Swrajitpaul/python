# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 16:44:00 2018

@author: swrajit
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    low = 0
    high = len(aStr)
    mid = (low+high)//2
    
    if mid == high or len(aStr) == 0:
        return False
    
    if aStr[mid] == char:
        return True
        
    elif char < aStr[mid]:
        return  isIn(char, aStr[low:mid])
    
    else:
        return  isIn(char, aStr[mid+1:high])
