#! /usr/bin/python3
#interpreter in the first line above

#Programmer: Amin Hasanzadeh
#Date: September 5 2018
#Purpose: Learning namespace and scope

print('First practice for scope')
myString = 'Outside Hello World'

def mainFunction():
    myString ='Hello World'
    print('myString = %s' % myString)
    return

mainFunction()
print('Global: myString = %s' % myString)   #myString ='Hello World' is not
#in the scope

print('Second practice for scope')
myString = 'Global myString'

def globalFunction():
    myString = 'Sub global myString'
    def localFunction():
        myString = 'Local myString'
        return
    localFunction()
    print('Sub myString = %s' % myString)

globalFunction()
print('Global myString = %s' % myString)

print('Third practice for scope')
myString = 'Global myString'

def globalFunction():
    myString = 'Sub global myString'
    def localFunction():
        nonlocal myString
        myString = 'Local myString'
        return
    localFunction()
    print('Sub myString = %s' % myString)

globalFunction()
print('Global myString = %s' % myString)

print('Forth practice for scope')
myString = 'Global myString'

def globalFunction():
    myString = 'Sub global myString'
    def localFunction():
        global myString
        myString = 'Local myString'
        return
    localFunction()
    print('Sub myString = %s' % myString)

globalFunction()
print('Global myString = %s' % myString)

print('Fifth practice for scope')
myString = 'Global myString'

def globalFunction():
    global myString
    myString = 'Sub global myString'
    def localFunction():
        myString = 'Local myString'
        return
    localFunction()
    print('Sub myString = %s' % myString)

globalFunction()
print('Global myString = %s' % myString)
