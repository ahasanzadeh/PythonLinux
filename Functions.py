#! /usr/bin/python3
#interpreter in the first line above

#Programmer: Amin Hasanzadeh
#Date: September 5 2018
#Purpose: Learning functions

def function1 (myString):
    'This is my function one'
    print('myString is %s' % myString)
    return

function1('Hello world')

MY_NAME = 'Amin Hasanzadeh'
function1(MY_NAME)

#:8,16s/^/# /&    to comment lines 8 to 16

def addNumbers(myNumber1 , myNumber2):
    'Add numbers'
    print('myNumber1 = %d' % myNumber1)
    print('myNumber2 = %d' % myNumber2)
    return myNumber1 + myNumber2

myResult = addNumbers(4 , 5)
print('myResult = %d' % myResult)

myResult = addNumbers(myNumber1 = 4 , myNumber2 = 5)
print('myResult = %d' % myResult)

myResult = addNumbers(myNumber2 = 5 , myNumber1 = 4)
print('myResult = %d' % myResult)

#default value for myNumber2
def addNumbers(myNumber1 , myNumber2 = 7):
    'Add numbers'
    print('myNumber1 = %d' % myNumber1)
    print('myNumber2 = %d' % myNumber2)
    return myNumber1 + myNumber2

myResult = addNumbers(4 , 5)
print('myResult = %d' % myResult)

#no calling second argument and default value shows up
myResult = addNumbers(4)
print('myResult = %d' % myResult)

#by value: if you have a variable outside the function, and then you pass that 
#variable, and then you change the value of that variable inside the function, 
#and when it exits the function, the variable that is outside the function have 
#not changed, that is called by value.

MY_NUMBER = 2

def numberChange(myNumber):
    'change number'
    myNumber = 4
    print('myNumber = %d' % myNumber)
    return

print('MY_NUMBER = %d' % MY_NUMBER)
numberChange(MY_NUMBER)
print('MY_NUMBER = %d' % MY_NUMBER)

#by reference:if you change the value inside the function, that is that been 
#passed it will also change the value outside.

MY_NUMBER = [2]

def numberChange(myNumber):
    'change number'
    myNumber.append(4)    #go to linux shell, and type python3 first, and 
    #interactive python command line type myNumber = [2] and then dir(myNumber
    #), you will see all possible function like append there.
    print('myNumber = ')
    print(myNumber)
    return

print('MY_NUMBER = ')
print(MY_NUMBER)
numberChange(MY_NUMBER)
print('MY_NUMBER = ')
print(MY_NUMBER)

