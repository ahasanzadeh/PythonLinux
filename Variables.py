#! /usr/bin/python3  
#interpreter in the first line above

import os

#Programmer: Amin Hasanzadeh
#Date: August 29 2018
#Purpose: Learning how to handle variables  

FIRST_NAME = "Amin"
LAST_NAME = "Hasanzadeh"
ONE_BLANK = " "

MY_INT_1 = 3
MY_INT_2 = 5

MY_FLOAT_1 = 3.5
MY_FLOAT_2 = 5.2

print(os.uname())
print("Hello World")
print('Amin Hasanzadeh')
print(FIRST_NAME)
print(LAST_NAME)
print(FIRST_NAME + ONE_BLANK + LAST_NAME)

print(MY_INT_1 + MY_INT_2)
print(MY_FLOAT_1 + MY_FLOAT_2)
print("What is the number?" + ONE_BLANK + repr( MY_INT_1))
print("What is the number?" + ONE_BLANK + repr( MY_INT_1) + repr(MY_FLOAT_1))
print("What is the number?" + ONE_BLANK + repr( MY_INT_1 + MY_FLOAT_1))
