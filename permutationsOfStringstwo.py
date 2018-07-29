# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 00:18:26 2018

@author: swrajit
"""

class Solution:
    
    
    def __init__(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        temp = []
        ls = 0   
        self.p(temp,nums)
        l = []
        print(ls)
        
    def p(self, a,b):
        global ls
        ls += 1
        if len(a) == len(b):
            l =[]
            l.append(a)
            print(l)
        else:
            for i in b:
                if i not in a:
                    a.append(i)
                    self.p(a,b)
                    a.remove(i)
        
 
b = []               
c =['A','B', 'C', 'D']
a = Solution(c)