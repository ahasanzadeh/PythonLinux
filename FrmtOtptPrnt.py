#! /usr/bin/python3  
#interpreter in the first line above

#Programmer: Amin Hasanzadeh
#Date: September 1 2018
#Purpose: Learning formatting output with print() function

MY_FIRST_NAME = 'John Stevenson'
MY_SECOND_NAME = "Alice Lee"

MY_FIRST_NUMBER = 4
MY_SECOND_NUMBER = 7

print(MY_FIRST_NAME + MY_SECOND_NAME)

print(MY_FIRST_NAME + ' ' + MY_SECOND_NAME)
print(MY_FIRST_NAME + ',' + MY_SECOND_NAME)

print(MY_FIRST_NAME , MY_SECOND_NAME, sep='|')
print(MY_FIRST_NAME , MY_SECOND_NAME, sep=' <--> ')

print(MY_FIRST_NAME , MY_SECOND_NAME, MY_FIRST_NUMBER, MY_SECOND_NUMBER, sep=' <--> ')

print('Names are %s and %s' % (MY_FIRST_NAME, MY_SECOND_NAME))
print('Numbers are %d and %d' % (MY_FIRST_NUMBER, MY_SECOND_NUMBER))

print('Numbers are {0} and {1}' .format(MY_FIRST_NUMBER, MY_SECOND_NUMBER))
print('Numbers are {1} and {0}' .format(MY_FIRST_NUMBER, MY_SECOND_NUMBER))

print('Numbers are %4d and %4d' % (4, 25))   #aligning by add %4d
print('Numbers are %4d and %4d' % (100, 5))

print('First name is %20s' % MY_FIRST_NAME)   #aligning by add %20s
print('Second name is %20s' % MY_SECOND_NAME)

