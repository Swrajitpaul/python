# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 13:00:47 2018

@author: swrajit
"""


def fibeff(n, d): 
    global count
    count += 1
    if n in d: 
        return d[n] 
    else: 
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d) 
        d[n] = ans 
        return ans

d = {1:1, 2:2} 
print(fib_efficient(6, d))