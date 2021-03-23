#! /usr/bin/python3
#interpreter in the first line above

#Programmer: Amin Hasanzadeh
#Date: September 2 2018
#Purpose: Learning user-keyboard input using input() function

MY_FIRST_STRING = 'hello'
MY_SECOND_STRING = 'world'

MY_FIRST_INTEGER = 5
MY_SECOND_INTEGER = 2

if(MY_FIRST_INTEGER == MY_SECOND_INTEGER):
    print('MY_FIRST_INTEGER is equal to MY_SECOND_INTEGER')

if(MY_FIRST_INTEGER > MY_SECOND_INTEGER):
    print('MY_FIRST_INTEGER is greater than MY_SECOND_INTEGER')

if(MY_FIRST_INTEGER < MY_SECOND_INTEGER):
    print('MY_FIRST_INTEGER is less than to MY_SECOND_INTEGER')


if(MY_FIRST_INTEGER == MY_SECOND_INTEGER):
    print('MY_FIRST_INTEGER is equal to MY_SECOND_INTEGER')
elif(MY_FIRST_INTEGER > MY_SECOND_INTEGER):
    print('MY_FIRST_INTEGER is greater than MY_SECOND_INTEGER')
else:
    print('MY_FIRST_INTEGER is less than to MY_SECOND_INTEGER')

if(MY_FIRST_STRING == MY_SECOND_STRING):
    print('MY_FIRST_STRING is same as MY_SECOND_STRING')
elif(MY_FIRST_STRING != MY_SECOND_STRING):
    print('MY_FIRST_STRING is not same as MY_SECOND_STRING')

