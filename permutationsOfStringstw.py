# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 00:18:26 2018

@author: swrajit
"""


def helper(self, nums, start, ret, n):
    if start == n-1:
        ret.append(list(nums))
        return 
    
    swaped = set()
    
    for i in range(start, n):
        if not nums[i] in swaped:
            swaped.add(nums[i])
        else:
            continue
        nums[start], nums[i] = nums[i], nums[start]
        self.helper(nums, start+1, ret, n)
        nums[i], nums[start] = nums[start], nums[i]
    
def permuteUnique(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ret = []
    self.helper(nums, 0, ret, len(nums))
    return ret
                a.remove(i)
        
 
b = []               
c =['A','B', 'C', 'D']
a = Solution(c)