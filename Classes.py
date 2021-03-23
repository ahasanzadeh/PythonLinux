#! /usr/bin/python3
#Interpreter in the first line above

#Programmer: Amin Hasanzadeh
#Date: September 6 2018
#Purpose: Learning classes 

print('###############First practice on classes###############')
class myClass:
    def __init__(self):
        print('Hello world')

myClassVariable = myClass()

print('###############Second practice on classes###############')
class myClass:
    def __init__(self, myNumber1):
        print('Hello world')
        print('myNumber = %d' % myNumber1)

myClassVariable = myClass(5)

print('###############Third practice on classes###############')
class myClass:
    def __init__(self, myNumber1, myNumber2):
        print('Hello world')
        print('myNumber1, myNumber2 = %d %d' % (myNumber1, myNumber2))

myClassVariable = myClass(5, 7)

print('###############Forth practice on classes###############')
class myClass:
    myNumber1 = 0
    myNumber2 = 0
    myNumber3 = 0
    def __init__(self):
        print('Hello world')
    def getData(self, myNumber4, myNumber5):
        self.myNumber1 = myNumber4     #self.myNumber1 refers to myNumber1
        self.myNumber2 = myNumber5     #above
    def addNumbers(self):
        self.myNumber3 = self.myNumber1 + self.myNumber2
    def printSum(self):
        print('Sum = %d' % self.myNumber3)

myClassVariable = myClass()
myClassVariable.getData(3, 4)
myClassVariable.addNumbers()
myClassVariable.printSum()

#Is there any private variable thing in python like C++, research __myVar

print('###############Iinheritance from base class###############')
class myNewClass(myClass):
    def __init__(self):
        print('Hello new class')
    def printMessage(self):
        print('My new class')

myClassVariable = myNewClass()    #Inheritance
myClassVariable.getData(3, 4)
myClassVariable.addNumbers()
myClassVariable.printSum()
myClassVariable.printMessage()

print('##############Fifth practice on classes (why class)##############')
class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

print(emp1)
print(emp2)

emp1.first = 'Corey'
emp1.last = 'Schafer'
emp1.email = 'Corey.Schafer@company.com'
emp1.pay = 50000

emp2.first = 'Test'
emp2.last = 'User'
emp2.email = 'Test.User@company.com'
emp2.pay = 60000

print(emp1.email)
print(emp2.email)

print('#####Sixth practice on classes (use class, instant variable)#####')
class Employee:
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', '60000')

print(emp1.email)
print(emp2.email)

print('Fisrt employee name: %s %s' % (emp1.first, emp1.last))
print('Second employee name: {} {}' .format(emp2.first, emp2.last))
print(emp1.fullName())   #calling method or function, need ()
print(Employee.fullName(emp2))  #right way, compare with above one

print('#####Seventh practice on classes (use class, class variable)#####')
class Employee:
    RAISE_AMOUNT = 1.04
    numberOfEmployee = 0
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numberOfEmployee += 1

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)
        #self.pay = int(self.pay * Employee.RAISE_AMOUNT)  #works too, but 
        #self.RAISE_AMOUNT is preferable, because it can be overwright by 
        #each instance of class like emp1 or emp2

print('##############################################')
print(Employee.numberOfEmployee)

emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1.pay)
emp1.applyRaise()
print(emp1.pay)

print('##############################################')
print(Employee.RAISE_AMOUNT)
print(emp1.RAISE_AMOUNT)
print(emp2.RAISE_AMOUNT)

print('##############################################')
print(emp1.__dict__)   #Namespace for Employee one, no RAISE_AMOUNT
print(Employee.__dict__)   #Namespace for Employee one, with RAISE_AMOUNT

print('##############################################')
emp1.RAISE_AMOUNT = 1.05
print(Employee.RAISE_AMOUNT)
print(emp1.RAISE_AMOUNT)
print(emp2.RAISE_AMOUNT)
print(emp1.__dict__)   #Namespace for Employee one, with RAISE_AMOUNT

print('##############################################')
Employee.RAISE_AMOUNT = 1.03
print(Employee.RAISE_AMOUNT)
print(emp1.RAISE_AMOUNT)
print(emp2.RAISE_AMOUNT)

print('##############################################')
print(Employee.numberOfEmployee)

print('###Eighth on classes (diff. regular, class and static methods)###')
#regular method in a class automatically take "self" instance as first 
#argument, we are going to change this to take class as first argument, 
#and we are ging to change regular method into class method,we need to add
#a decorator "@classmethod"
class Employee:
    RAISE_AMOUNT = 1.04
    numberOfEmployee = 0
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numberOfEmployee += 1

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)
        #self.pay = int(self.pay * Employee.RAISE_AMOUNT)  #works too, but 
        #self.RAISE_AMOUNT is preferable, because it can be overwright by 
        #each instance of class like emp1 or emp2
    @classmethod 
    def setRaiseAmount(cls, raiseAmount):
        cls.RAISE_AMOUNT = raiseAmount

print('##############################################')
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(Employee.RAISE_AMOUNT)
print(emp1.RAISE_AMOUNT)
print(emp2.RAISE_AMOUNT)

print('##############################################')
Employee.setRaiseAmount(1.05)

print(Employee.RAISE_AMOUNT)
print(emp1.RAISE_AMOUNT)
print(emp2.RAISE_AMOUNT)

print('##############################################')
emp1.setRaiseAmount(1.03)

print(Employee.RAISE_AMOUNT)
print(emp1.RAISE_AMOUNT)
print(emp2.RAISE_AMOUNT)

print('##############################################')
empString1 = 'John-Doe-70000'
empString2 = 'Steve-Smith-30000'
empString3 = 'Jane-Dre-90000'

first, last, pay = empString1.split('-')
empNew1 = Employee(first, last, pay)

first, last, pay = empString2.split('-')
empNew2 = Employee(first, last, pay)

first, last, pay = empString3.split('-')
empNew3 = Employee(first, last, pay)

print(empNew1.first)
print(empNew2.email)
print(empNew3.pay)

print('###Ninth on classes (class method as alternative constructor)###')
class Employee:
    RAISE_AMOUNT = 1.04
    numberOfEmployee = 0
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numberOfEmployee += 1

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)
        #self.pay = int(self.pay * Employee.RAISE_AMOUNT)  #works too, but 
        #self.RAISE_AMOUNT is preferable, because it can be overwright by 
        #each instance of class like emp1 or emp2
    @classmethod 
    def setRaiseAmount(cls, raiseAmount):
        cls.RAISE_AMOUNT = raiseAmount
    @classmethod
    def fromString(cls, empString):
        first, last, pay = empString.split('-')
        return cls(first, last, pay)
        #class method as alternative constructor: you can use class 
        #method in order to provide multiple ways of creating our objects

print('##############################################')
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

empString1 = 'John-Doe-70000'
empString2 = 'Steve-Smith-30000'
empString3 = 'Jane-Dre-90000'

empNew1 = Employee.fromString(empString1)
empNew2 = Employee.fromString(empString2)
empNew3 = Employee.fromString(empString3)

print(empNew1.first)
print(empNew2.email)
print(empNew3.pay)

print('###############Tenth on classes (static method)###############')
#when working with classes, regular method automatically passes "self"
#instance as the first argument, and class method automatically passes 
#class "cls" as the first argument, and the static method does not pass
#anything automatically, it does not pass instance or class so really they 
#behave just like regular function except we include them inour classes 
#because it has some logical connection with the class

class Employee:
    RAISE_AMOUNT = 1.04
    numberOfEmployee = 0
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.numberOfEmployee += 1

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)
        #self.pay = int(self.pay * Employee.RAISE_AMOUNT)  #works too, but 
        #self.RAISE_AMOUNT is preferable, because it can be overwright by 
        #each instance of class like emp1 or emp2
    @classmethod 
    def setRaiseAmount(cls, raiseAmount):
        cls.RAISE_AMOUNT = raiseAmount
    @classmethod
    def fromString(cls, empString):
        first, last, pay = empString.split('-')
        return cls(first, last, pay)
        #class method as alternative constructor: you can use class 
        #method in order to provide multiple ways of creating our objects
    @staticmethod
    def isWorkDay(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True      #in weekday method/function Monday=0 ... Sunday=6
        #isWorkDay has logical connection to Employee class but it does 
        #not actually depend on any specific instance or class variable
        #so the method should be static method, if you do not access the 
        #instance "self" or class "cls" anywhere within the function like 
        #other functions/methods in the Employee

import datetime
myDate = datetime.date(2016, 7, 10)

print(Employee.isWorkDay(myDate))

print('########Eleventh on classes (inheritance and subclasses)########')
class Employee:
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)

class Developer(Employee):
    #pass    #just inherit
    RAISE_AMOUNT = 1.10   #change raise here

print('##############################################')
dev1 = Employee('Corey', 'Schafer', 50000)
dev2 = Employee('Test', 'User', 60000)

print(dev1.email)
print(dev2.email)

print('##############################################')
dev1 = Developer('Corey', 'Schafer', 50000)
dev2 = Developer('Test', 'User', 60000)

print(dev1.email)
print(dev2.email)

print('##############################################')
#print(help(Developer))   #try this line

print('##############################################')
print(dev1.pay)
dev1.applyRaise()
print(dev1.pay)

print('##############################################')
dev1 = Employee('Corey', 'Schafer', 50000)
print(dev1.pay)
dev1.applyRaise()
print(dev1.pay)

print('########Twelveth on classes (inheritance and subclasses)########')
class Employee:
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)

class Developer(Employee):
    #pass    #just inherit
    RAISE_AMOUNT = 1.10   #change raise here
    def __init__(self, first, last, pay, progLang): 
        super().__init__(first, last, pay)
        #Employee.__init__(self, first, last, pay)   #alternative,but
        #above one is more maintainable
        self.progLang = progLang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None): 
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    def addEmployee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def removeEmployee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def printEmployees(self):
        for emp in self.employees:
            print('-->', emp.fullName())

print('##############################################')
dev1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev2 = Developer('Test', 'User', 60000, 'Java')

print(dev1.progLang)
print(dev2.progLang)

print('##############################################')
mgr1 = Manager('Sue', 'Smith', 90000, [dev1])

print(mgr1.email)

mgr1.addEmployee(dev2)
mgr1.printEmployees()

print('##############################################')
mgr1.removeEmployee(dev1)
mgr1.printEmployees()

print('##############################################')
print(isinstance(mgr1, Manager))
print(isinstance(mgr1, Developer))
print(issubclass(Developer, Employee))

print('########13th on classes (special magic/dunder methods)########')
class Employee:
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)
    def __repr__(self):   #unambiguous representation of theobject and
        #should be used for debugging and logging and things like that,
        #it is really meant to be seen by other devlopers
        return "Employee('{}', '{}', {})".format(self.first, self.last,
                self.pay)
    def __str__(self):    #more of a readable representation of an object
        #and is meant to be used as display tp the end-user
        return '{} - {}'.format(self.fullName(), self.email)

print('##############################################')
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1)    #without repr method, output is nonsense; if there is no
                #str method, it shows Employee('Corey', 'Schafer', 50000),
                #if str exist, it shows Employee name: Corey Schafer -
                #Corey.Schafer@company.com

print('##############################################')
print(repr(emp1))
print(emp1.__repr__())   #same as above line
print('##############################################')
print(str(emp1))
print(emp1.__str__())   #same as above line   
print('##############################################')
#another useful dunder
print(1+2)
print(int.__add__(1, 2))   #same as above line, work in background  
print('a'+'b')
print(str.__add__('a', 'b'))   #same as above line, work in background  
print(len('test'))
print('test'.__len__())

print('########14th on classes (special magic/dunder methods)########')
class Employee:
    RAISE_AMOUNT = 1.04
    def __init__(self, first, last, pay):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullName(self):   # need self (instant argument)
        return 'Employee name: {} {}' .format(self.first, self.last)
    def applyRaise(self):
        self.pay = int(self.pay * self.RAISE_AMOUNT)
    def __repr__(self):   #unambiguous representation of theobject and
        #should be used for debugging and logging and things like that,
        #it is really meant to be seen by other devlopers
        return "Employee('{}', '{}', {})".format(self.first, self.last,
                self.pay)
    def __str__(self):    #more of a readable representation of an object
        #and is meant to be used as display tp the end-user
        return '{} - {}'.format(self.fullName(), self.email)
    def __add__(self, other):
        return  self.pay + other.pay
    def __len__(self):
        return len(self.fullName())

print('##############################################')
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Test', 'User', 60000)

print(emp1.fullName())
print(len(emp1))
print(emp1 + emp2)  #without dunder add, it gives error; with shows 110000

print('##15th on classes (property decorators: geter, seter, deleters)##')
class Employee:
    def __init__(self, first, last):   #initialization or constructor
        self.first = first   #self.fname = first
        self.last = last

    @property
    def email(self): 
        return '{}.{}@company.com' .format(self.first, self.last)
    @property
    def fullName(self):   # need self (instant argument)
        return '{} {}' .format(self.first, self.last)
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    @fullName.deleter
    def fullName(self):
        print('Delete Name!')
        self.first = None
        self.last = None

print('##############################################')
emp1 = Employee('Corey', 'Schafer')
emp2 = Employee('Test', 'User')

emp1.first = 'Jim'   #with till now structure of class above, email shows 
                     #old first name, so we need property decorator above,
                     #with property decorator, you access email as
                     #attribute like before, not as a method email(),
                     #define email as  method and use as attribute 
print(emp1.first)
print(emp1.email)
print(emp1.fullName)   #here, we used fullname as attribute by decorator,
                       # no need () after fullname

print('##############################################')
#use setter
emp1.fullName = 'Corey Schafer'

print(emp1.first)
print(emp1.email)
print(emp1.fullName) 

print('##############################################')
#use deleter
del emp1.fullName 
