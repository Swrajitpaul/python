# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 17:59:52 2018

@author: swrajit
"""

num = 101
st = []
while(num // 7 != 0):
    st.append(num%7)
    num = num // 7

st.append(num % 7)
st.reverse()
s = ''

for e in st:
    s += str(e)

print(s)
