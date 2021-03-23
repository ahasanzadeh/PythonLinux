#! /usr/bin/python3

#Programmer: Amin Hasanzadeh
#Date: September 4 2018
#Purpose: Learning while and for loop statements

MY_FIRST_NUMBER = 10
i = 0

while (i < MY_FIRST_NUMBER):
    print('i = %d' % i)
    i += 1
else:
    print('Final i = %d' % i)
    print('Done!')

for i in range (1 , 10):
    print('Number is %d' % i)
else:
    print('Final i = %d' % i)
    print('Done!')

jobs = ['programmer', 'developer', 'engineer', 'help desk', 'system admin']

for jobName in jobs:
    print('Title: %s' % jobName)
else:
    print('Done!')
