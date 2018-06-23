# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 21:39:18 2018

@author: swrajit
"""

print('Please think of a number between 0 and 100!')
low = 0
high = 100
guess = (high+low)//2
st =""
while(True):
    print("Is your secret number "+ str(guess) + '?')
    st = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    while(st != 'c' and st != 'h' and st != 'l'):
        print('Sorry, I did not understand your input.')
        print("Is your secret number "+ str(guess) + '?')
        st = input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correctly.')
    if(st =='c'):
        break;
    elif(st =='l'):
        low = guess
        guess = (high + low)//2
    elif(st =='h'):
        high= guess
        guess=(high + low)//2
print('Game over. Your secret number was: '+ str(guess))
