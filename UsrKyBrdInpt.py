#! /usr/bin/python3  
#interpreter in the first line above

#Programmer: Amin Hasanzadeh
#Date: August 30 2018
#Purpose: Learning user-keyboard input using input() function 

myName = input("What is your name? ")

print('Hello ' + myName)

print(myName + ', Let\'s add two numbers!')   #backslash for using sigle quote in middle of sentence inside two sigle quotes

myFirstNumber = input('Enter the first number: ')
mySecondNumber = input('Enter the second number: ')

sumNumbers = int(myFirstNumber) + int(mySecondNumber)

print('The total of myFirstNumber and mySecondNumber is ' + repr(sumNumbers))
