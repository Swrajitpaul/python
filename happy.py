# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 13:15:58 2018

@author: swrajit
"""

def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    ls = []
    while n!= 1:
        if n not in ls:
            ls.append(n)
            st = str(n)
            n = 0
            for c in st:
                num = int(c)
                n += num ** 2
        else:
            return False
    
    return True
    
isHappy(2)