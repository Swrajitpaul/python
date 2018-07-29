# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 11:06:39 2018

@author: swrajit
"""
s = '(1+(4+5+2)-3)+(6+8)'
ls = []
total = 0

for i in range(len(s)-1, 0, -1):
    if s[i] == ')':
        temp = 0
        popped = ls.pop()
        while popped != '(':
            if popped == '+':
                temp += int(ls.pop())
                popped = ls.pop()
                
            elif popped == '-':
                temp -= int(ls.pop())
                popped = ls.pop()
                
            
            else:
                temp = int(popped)
                popped = ls.pop()
        
        ls.append(temp) 
    
    else:
        if s[i] == ' ':
            continue
        ls.append(i)



            
            
print(total)