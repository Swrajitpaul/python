# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 20:37:24 2018

@author: swrajit
insertion sort class
"""

class insertionSort(object):
    def __init__(self, arr):
        # arr is a list 
        self.Array = arr
        self.lst = []
        
    def sort(self):
        for i in range(1, len(self.Array)):
            key = self.Array[i]
        