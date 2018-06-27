# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 12:45:57 2018

@author: swrajit
"""

def largest(adict):
    keys = animals.keys()
    largest = 0
    ke = ''
    
    for k in keys:
        
        liVal = animals[k]
        temp = 0
        
        for v in liVal:
            temp = temp + 1
        
        if temp >= largest:
            largest = temp
            ke = k 
    return ke 

print(largest(animals))      
            