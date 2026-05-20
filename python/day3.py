# =========================================================
# EXCEPTION HANDLING IN PYTHON
# =========================================================


# =========================================================
# WHAT IS EXCEPTION HANDLING?
# =========================================================

# When we run a Python program,
# different types of errors can occur.

# Examples:
# - Syntax Error
# - Name Error
# - ZeroDivisionError
# - ValueError
# etc.


# Exceptions are raised when:
# Program syntax is correct,
# but runtime error occurs.

# These errors change the normal flow
# of the program.


# =========================================================
# SYNTAX ERROR
# =========================================================

# Syntax Errors cannot be handled.

# Example:

# print("Hello"

# Output:
# SyntaxError


# Reason:
# Python interpreter cannot understand
# incorrect syntax.



# =========================================================
# RUNTIME EXCEPTION
# =========================================================

# Runtime exceptions CAN be handled.

# Example:

# print(10 / 0)

# Output:
# ZeroDivisionError



# =========================================================
# WHY EXCEPTION HANDLING?
# =========================================================

# Without Exception Handling:
# Program crashes immediately.

# With Exception Handling:
# Program continues execution safely.



# =========================================================
# TRY BLOCK
# =========================================================

# try block contains risky code.

try:

    print(10 / 2)

except:

    print("Error Occurred")

# Output:
# 5.0


# No exception occurred,
# so except block did not run.



# =========================================================
# EXCEPT BLOCK
# =========================================================

# except block handles exception.

try:

    print(10 / 0)

except:

    print("Exception Handled")

# Output:
# Exception Handled



# =========================================================
# SPECIFIC EXCEPTION HANDLING
# =========================================================

# Handling specific exception type.

try:

    number = int("abc")

except ValueError:

    print("Invalid Value")

# Output:
# Invalid Value



# =========================================================
# MULTIPLE EXCEPT BLOCKS
# =========================================================

try:

    number = int(input("Enter Number : "))
    result = 10 / number

    print(result)

except ValueError:

    print("Please Enter Integer Value")

except ZeroDivisionError:

    print("Cannot Divide By Zero")

# Example Input:
# 0

# Output:
# Cannot Divide By Zero



# =========================================================
# UNIVERSAL EXCEPTION CATCHER
# =========================================================

# Exception catches every exception.

try:

    print(x)

except Exception as error:

    print(f"Error : {error}")

# Output:
# Error : name 'x' is not defined



# =========================================================
# ELSE BLOCK
# =========================================================

# else block executes only if
# no exception occurs.

try:

    number = int(input("Enter Number : "))

    print(number)

except ValueError:

    print("Invalid Input")

else:

    print("Program Executed Successfully")

# Example Input:
# 10

# Output:
# 10
# Program Executed Successfully



# =========================================================
# FINALLY BLOCK
# =========================================================

# finally block ALWAYS executes.

try:

    print(10 / 2)

except:

    print("Error")

finally:

    print("Finally Block Executed")

# Output:
# 5.0
# Finally Block Executed



# =========================================================
# FINALLY WITH ERROR
# =========================================================

try:

    print(10 / 0)

except:

    print("Exception Handled")

finally:

    print("This Will Always Execute")

# Output:
# Exception Handled
# This Will Always Execute



# =========================================================
# REAL LIFE EXAMPLE
# =========================================================

# File handling example.

try:

    file = open("data.txt")

    print(file.read())

except FileNotFoundError:

    print("File Does Not Exist")

finally:

    print("Program Ended")

# Output:
# File Does Not Exist
# Program Ended



# =========================================================
# RAISE KEYWORD
# =========================================================

# raise is used to create custom errors.

age = -5

if age < 0:

    raise ValueError("Age Cannot Be Negative")

# Output:
# ValueError: Age Cannot Be Negative



# =========================================================
# CUSTOM EXCEPTION MESSAGE
# =========================================================

password = "123"

if len(password) < 6:

    raise Exception("Password Too Short")

# Output:
# Exception: Password Too Short



# =========================================================
# USER DEFINED EXCEPTION
# =========================================================

# Creating our own exception class.

class InvalidAgeError(Exception):
    pass


age = -10

try:

    if age < 0:

        raise InvalidAgeError("Invalid Age")

except InvalidAgeError as error:

    print(error)

# Output:
# Invalid Age



# =========================================================
# COMPLETE EXAMPLE
# =========================================================

try:

    number1 = int(input("Enter First Number : "))
    number2 = int(input("Enter Second Number : "))

    result = number1 / number2

except ValueError:

    print("Please Enter Valid Numbers")

except ZeroDivisionError:

    print("Division By Zero Not Allowed")

else:

    print(f"Result : {result}")

finally:

    print("Execution Completed")

# Example Input:
# 10
# 2

# Output:
# Result : 5.0
# Execution Completed



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Exception changes normal flow of program.
# 2. Syntax Errors cannot be handled.
# 3. Runtime errors can be handled.
# 4. try contains risky code.
# 5. except handles exception.
# 6. else runs if no exception occurs.
# 7. finally always executes.
# 8. raise creates custom error.
# 9. Exception class catches all exceptions.
# 10. Exception handling prevents program crash.



# =========================================================
# END OF EXCEPTION HANDLING
# =========================================================


# =========================================================
# FILE HANDLING IN PYTHON
# =========================================================

# File Handling in Python deals with files.

# It allows us to:
# 1. Create Files
# 2. Read Files
# 3. Update Files
# 4. Delete Files

# These operations are also called:
# CRUD Operations

# C -> Create
# R -> Read
# U -> Update
# D -> Delete



# =========================================================
# OPENING A FILE
# =========================================================

# open() is used to open a file.

# Syntax:
# open(file_location, mode)

# Parameters:
# 1. File Location
# 2. File Mode



# =========================================================
# FILE MODES
# =========================================================

# "r" -> Read Mode
# "a" -> Append Mode
# "w" -> Write Mode
# "x" -> Create Mode



# =========================================================
# READ MODE ("r")
# =========================================================

# "r" reads existing file.
# Error occurs if file does not exist.

file = open("demo.txt", "r")

print(file.read())

file.close()

# Example Output:
# Hello Ruchit
# Welcome to Python


# Explanation:
# read() reads complete file content.



# =========================================================
# WRITE MODE ("w")
# =========================================================

# "w" overwrites existing content.
# Creates file if it does not exist.

file = open("demo.txt", "w")

file.write("Python File Handling")

file.close()

print("Data Written Successfully")

# Output:
# Data Written Successfully


# File Content:
# Python File Handling



# =========================================================
# APPEND MODE ("a")
# =========================================================

# "a" adds data at end of file.
# Creates file if file does not exist.

file = open("demo.txt", "a")

file.write("\nAppending New Data")

file.close()

print("Data Appended Successfully")

# Output:
# Data Appended Successfully


# File Content:
# Python File Handling
# Appending New Data



# =========================================================
# CREATE MODE ("x")
# =========================================================

# "x" creates new file.
# Error occurs if file already exists.

# file = open("newfile.txt", "x")

# print("File Created Successfully")

# Output:
# File Created Successfully


# If file already exists:
# FileExistsError



# =========================================================
# CLOSING FILE
# =========================================================

# close() closes the file.

file = open("demo.txt", "r")

print(file.read())

file.close()

# Output:
# File Content Printed


# Why close()?
# - Saves memory
# - Prevents file corruption



# =========================================================
# WITH OPEN()
# =========================================================

# with automatically closes file.

with open("demo.txt", "r") as file:

    data = file.read()

    print(data)

# Output:
# Python File Handling
# Appending New Data


# Explanation:
# No need to manually write close()



# =========================================================
# READING FILE LINE BY LINE
# =========================================================

with open("demo.txt", "r") as file:

    for line in file:

        print(line)

# Output:
# Python File Handling
# Appending New Data



# =========================================================
# read()
# =========================================================

# read() reads complete file.

with open("demo.txt", "r") as file:

    print(file.read())

# Output:
# Complete File Content



# =========================================================
# readline()
# =========================================================

# readline() reads one line at a time.

with open("demo.txt", "r") as file:

    print(file.readline())

# Output:
# First Line



# =========================================================
# readlines()
# =========================================================

# readlines() returns all lines in list.

with open("demo.txt", "r") as file:

    print(file.readlines())

# Output:
# ['Line 1\n', 'Line 2\n']



# =========================================================
# WRITING MULTIPLE LINES
# =========================================================

lines = [
    "Python\n",
    "Machine Learning\n",
    "Artificial Intelligence\n"
]

with open("demo.txt", "w") as file:

    file.writelines(lines)

print("Multiple Lines Written")

# Output:
# Multiple Lines Written



# =========================================================
# FILE POINTER FUNCTIONS
# =========================================================

# tell() -> tells current cursor position
# seek() -> changes cursor position

with open("demo.txt", "r") as file:

    print(file.tell())

    # Output:
    # 0

    file.read(5)

    print(file.tell())

    # Output:
    # 5

    file.seek(0)

    print(file.tell())

    # Output:
    # 0



# =========================================================
# EXCEPTION HANDLING IN FILES
# =========================================================

try:

    with open("unknown.txt", "r") as file:

        print(file.read())

except FileNotFoundError:

    print("File Does Not Exist")

# Output:
# File Does Not Exist



# =========================================================
# DELETE FILE
# =========================================================

# os module is required.

import os

# os.remove("demo.txt")

# Output:
# File Deleted Successfully


# If file does not exist:
# FileNotFoundError



# =========================================================
# CHECK FILE EXISTS
# =========================================================

import os

if os.path.exists("demo.txt"):

    print("File Exists")

else:

    print("File Does Not Exist")

# Output:
# File Exists



# =========================================================
# CREATE FOLDER
# =========================================================

import os

# os.mkdir("MyFolder")

# Output:
# Folder Created



# =========================================================
# REMOVE FOLDER
# =========================================================

import os

# os.rmdir("MyFolder")

# Output:
# Folder Removed



# =========================================================
# PROJECT : FILE CRUD SYSTEM
# =========================================================

# Simple File Handling Project

while True:

    print("\n===== FILE HANDLING PROJECT =====")

    print("1. Create File")
    print("2. Read File")
    print("3. Append File")
    print("4. Delete File")
    print("5. Exit")

    choice = input("Enter Choice : ")

    # CREATE FILE
    if choice == "1":

        filename = input("Enter File Name : ")

        data = input("Enter Data : ")

        with open(filename, "w") as file:

            file.write(data)

        print("File Created Successfully")


    # READ FILE
    elif choice == "2":

        filename = input("Enter File Name : ")

        try:

            with open(filename, "r") as file:

                print(file.read())

        except FileNotFoundError:

            print("File Not Found")


    # APPEND FILE
    elif choice == "3":

        filename = input("Enter File Name : ")

        data = input("Enter Data : ")

        with open(filename, "a") as file:

            file.write("\n" + data)

        print("Data Appended")


    # DELETE FILE
    elif choice == "4":

        filename = input("Enter File Name : ")

        if os.path.exists(filename):

            os.remove(filename)

            print("File Deleted")

        else:

            print("File Not Found")


    # EXIT
    elif choice == "5":

        print("Program Ended")

        break


    else:

        print("Invalid Choice")



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. File Handling performs CRUD operations.
# 2. open() opens a file.
# 3. "r" -> Read Mode
# 4. "w" -> Write Mode
# 5. "a" -> Append Mode
# 6. "x" -> Create Mode
# 7. with open() automatically closes file.
# 8. read(), readline(), readlines() are reading methods.
# 9. write() and writelines() are writing methods.
# 10. os module helps in file/folder operations.



# =========================================================
# END OF FILE HANDLING
# =========================================================


# =========================================================
# INTRODUCTION TO OOPs IN PYTHON
# =========================================================

# OOPs stands for:
# Object Oriented Programming

# OOPs is a programming paradigm
# based on Objects and Classes.



# =========================================================
# TYPES OF PROGRAMMING
# =========================================================

# 1. Imperative Programming
# 2. Functional Programming
# 3. Object Oriented Programming



# =========================================================
# IMPERATIVE PROGRAMMING
# =========================================================

# Writing code step by step manually.

a = 12
b = 12

print(a + b)

# Output:
# 24


# Problem:
# Code repetition increases in large programs.



# =========================================================
# FUNCTIONAL PROGRAMMING
# =========================================================

# Reusable functions are created.

def addition(a, b):

    return a + b


print(addition(12, 12))
print(addition(45, 45))

# Output:
# 24
# 90


# Advantage:
# Reusability of code.



# =========================================================
# OBJECT ORIENTED PROGRAMMING
# =========================================================

# In OOPs we create Classes and Objects.

# Class acts like blueprint.
# Object is real implementation.


class Addition:

    def add(self, a, b):

        print(a + b)


# Creating Object

obj = Addition()

obj.add(12, 12)

# Output:
# 24



# =========================================================
# WHAT IS A CLASS?
# =========================================================

# Class is a blueprint or prototype
# used to create objects.

# Example:
# Car Blueprint -> Class
# Real Car -> Object



# =========================================================
# CREATING A CLASS
# =========================================================

class Student:

    pass


print(Student)

# Output:
# <class '__main__.Student'>



# =========================================================
# WHAT IS AN OBJECT?
# =========================================================

# Object is an instance of class.

class Student:

    pass


# Creating Object

obj1 = Student()
obj2 = Student()

print(obj1)
print(obj2)

# Output:
# <__main__.Student object at ...>
# <__main__.Student object at ...>



# =========================================================
# ATTRIBUTES
# =========================================================

# Attributes are variables inside class/object.


class Student:

    name = "Ruchit"
    age = 20


obj = Student()

print(obj.name)
print(obj.age)

# Output:
# Ruchit
# 20



# =========================================================
# METHODS
# =========================================================

# Methods are functions inside class.


class Student:

    def greet(self):

        print("Welcome Student")


obj = Student()

obj.greet()

# Output:
# Welcome Student



# =========================================================
# SELF KEYWORD
# =========================================================

# self refers to current object.

class Student:

    def display(self):

        print("Self Represents Current Object")


obj = Student()

obj.display()

# Output:
# Self Represents Current Object



# =========================================================
# CONSTRUCTOR
# =========================================================

# Constructor initializes object automatically.

# __init__() is constructor method.

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


obj = Student("Ruchit", 20)

print(obj.name)
print(obj.age)

# Output:
# Ruchit
# 20



# =========================================================
# TYPES OF ACCESS MODIFIERS
# =========================================================

# 1. Public
# 2. Protected
# 3. Private



# =========================================================
# PUBLIC MEMBERS
# =========================================================

# Accessible everywhere.

class Student:

    def __init__(self):

        self.name = "Ruchit"


obj = Student()

print(obj.name)

# Output:
# Ruchit



# =========================================================
# PROTECTED MEMBERS
# =========================================================

# Protected members use single underscore (_)

class Student:

    def __init__(self):

        self._age = 20


obj = Student()

print(obj._age)

# Output:
# 20


# Note:
# Protected members should be accessed carefully.



# =========================================================
# PRIVATE MEMBERS
# =========================================================

# Private members use double underscore (__)

class Student:

    def __init__(self):

        self.__salary = 50000


obj = Student()

# print(obj.__salary)

# Output:
# AttributeError


# Accessing private member indirectly

print(obj._Student__salary)

# Output:
# 50000



# =========================================================
# INHERITANCE
# =========================================================

# One class acquires properties of another class.



# =========================================================
# SINGLE LEVEL INHERITANCE
# =========================================================

class Parent:

    def display(self):

        print("Parent Class")


class Child(Parent):

    pass


obj = Child()

obj.display()

# Output:
# Parent Class



# =========================================================
# MULTILEVEL INHERITANCE
# =========================================================

class GrandParent:

    def show(self):

        print("Grand Parent")


class Parent(GrandParent):

    pass


class Child(Parent):

    pass


obj = Child()

obj.show()

# Output:
# Grand Parent



# =========================================================
# super() FUNCTION
# =========================================================

# super() accesses parent class methods.

class Parent:

    def __init__(self):

        print("Parent Constructor")


class Child(Parent):

    def __init__(self):

        super().__init__()

        print("Child Constructor")


obj = Child()

# Output:
# Parent Constructor
# Child Constructor



# =========================================================
# POLYMORPHISM
# =========================================================

# One thing having many forms.

class Dog:

    def sound(self):

        print("Dog Barks")


class Cat:

    def sound(self):

        print("Cat Meows")


animals = [Dog(), Cat()]

for animal in animals:

    animal.sound()

# Output:
# Dog Barks
# Cat Meows



# =========================================================
# ENCAPSULATION
# =========================================================

# Wrapping data and methods together.

class Bank:

    def __init__(self):

        self.__balance = 1000


    def deposit(self, amount):

        self.__balance += amount


    def show_balance(self):

        print(self.__balance)


obj = Bank()

obj.deposit(500)

obj.show_balance()

# Output:
# 1500


# Balance is protected using encapsulation.



# =========================================================
# ABSTRACTION
# =========================================================

# Hiding implementation details.

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass


class Car(Vehicle):

    def start(self):

        print("Car Started")


obj = Car()

obj.start()

# Output:
# Car Started



# =========================================================
# DUNDER (MAGIC) METHODS
# =========================================================

# Dunder means Double Underscore Methods.

# Examples:
# __init__
# __str__
# __len__



# =========================================================
# __str__ METHOD
# =========================================================

class Student:

    def __init__(self, name):

        self.name = name


    def __str__(self):

        return f"Student Name : {self.name}"


obj = Student("Ruchit")

print(obj)

# Output:
# Student Name : Ruchit



# =========================================================
# __len__ METHOD
# =========================================================

class Demo:

    def __len__(self):

        return 5


obj = Demo()

print(len(obj))

# Output:
# 5



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. OOPs stands for Object Oriented Programming.
# 2. Class is blueprint for objects.
# 3. Object is instance of class.
# 4. Attributes are variables inside class.
# 5. Methods are functions inside class.
# 6. __init__() is constructor.
# 7. self represents current object.
# 8. Inheritance reuses code.
# 9. Polymorphism means many forms.
# 10. Encapsulation provides security.
# 11. Abstraction hides implementation.
# 12. Dunder methods are special methods.



# =========================================================
# END OF OOPs INTRODUCTION
# =========================================================


# =========================================================
# CLASS IN PYTHON
# =========================================================

# Class is like a blueprint or prototype.

# It defines what properties and behaviors
# an object should have.


# =========================================================
# REAL LIFE EXAMPLE
# =========================================================

# Example:
# BAG FACTORY

# Suppose a factory wants to manufacture bags.

# Before creating bags,
# factory first creates a blueprint.

# Blueprint contains:
# - Color
# - Brand
# - Price
# - Size

# Using that blueprint,
# many bags can be created.


# In Python:
# Blueprint  -> Class
# Real Bag   -> Object



# =========================================================
# CREATING A CLASS
# =========================================================

# To create a class,
# we use class keyword.

# Syntax:

# class ClassName:
#     pass


# Example:

class Bag:

    pass


print(Bag)

# Output:
# <class '__main__.Bag'>



# =========================================================
# WHAT IS pass?
# =========================================================

# pass is a placeholder.

# It means:
# "We will write code later"

class Student:

    pass



# =========================================================
# ATTRIBUTES AND METHODS
# =========================================================

# Attribute:
# Variable inside class.

# Method:
# Function inside class.



# =========================================================
# CREATING ATTRIBUTES
# =========================================================

class Bag:

    color = "Black"
    brand = "Nike"
    price = 2000


# Accessing attributes

print(Bag.color)
print(Bag.brand)
print(Bag.price)

# Output:
# Black
# Nike
# 2000



# =========================================================
# CREATING METHODS
# =========================================================

class Bag:

    def show(self):

        print("This is Bag Method")


# Creating Object

obj = Bag()

# Calling Method

obj.show()

# Output:
# This is Bag Method



# =========================================================
# ACCESSING ATTRIBUTES USING OBJECT
# =========================================================

class Bag:

    color = "Black"
    brand = "Nike"


# Creating Object

obj = Bag()

# Accessing Attributes

print(obj.color)
print(obj.brand)

# Output:
# Black
# Nike



# =========================================================
# WHY OBJECT IS NEEDED?
# =========================================================

# Object is real implementation of class.

# Class only defines blueprint.
# Object actually uses blueprint.



# =========================================================
# MULTIPLE OBJECTS
# =========================================================

class Student:

    college = "ABC College"


student1 = Student()
student2 = Student()

print(student1.college)
print(student2.college)

# Output:
# ABC College
# ABC College



# =========================================================
# USING CONSTRUCTOR
# =========================================================

# Constructor initializes values automatically.

class Bag:

    def __init__(self, color, brand, price):

        self.color = color
        self.brand = brand
        self.price = price


# Creating Objects

bag1 = Bag("Black", "Nike", 2000)
bag2 = Bag("Blue", "Puma", 1500)


print(bag1.color)
print(bag1.brand)
print(bag1.price)

# Output:
# Black
# Nike
# 2000


print(bag2.color)
print(bag2.brand)
print(bag2.price)

# Output:
# Blue
# Puma
# 1500



# =========================================================
# self KEYWORD
# =========================================================

# self refers to current object.

class Demo:

    def display(self):

        print("Self refers to current object")


obj = Demo()

obj.display()

# Output:
# Self refers to current object



# =========================================================
# ATTRIBUTE + METHOD TOGETHER
# =========================================================

class Car:

    brand = "BMW"

    def start(self):

        print(f"{self.brand} Car Started")


obj = Car()

obj.start()

# Output:
# BMW Car Started



# =========================================================
# CHANGING ATTRIBUTE VALUE
# =========================================================

class Student:

    name = "Ruchit"


obj = Student()

print(obj.name)

# Output:
# Ruchit


# Changing value

obj.name = "Rahul"

print(obj.name)

# Output:
# Rahul



# =========================================================
# CLASS VS OBJECT
# =========================================================

# CLASS
# - Blueprint
# - Template
# - Defines structure

# OBJECT
# - Real entity
# - Created using class
# - Uses class features



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Class is blueprint or prototype.
# 2. Object is created using class.
# 3. class keyword creates class.
# 4. pass is placeholder keyword.
# 5. Variable inside class is Attribute.
# 6. Function inside class is Method.
# 7. self refers to current object.
# 8. Constructor initializes object values.
# 9. Multiple objects can be created from one class.



# =========================================================
# END OF CLASS IN PYTHON
# =========================================================


# =========================================================
# OBJECTS IN PYTHON
# =========================================================

# Object is a real implementation of a class.

# We use Class blueprint to create Objects.



# =========================================================
# REAL LIFE EXAMPLE
# =========================================================

# BAG FACTORY

# Factory provides blueprint:
# - Material
# - Zips
# - Pockets

# Different companies provide requirements.

# Reebok Bag:
# Material -> Leather
# Zips -> Three
# Pockets -> Four

# Campus Bag:
# Material -> Leather
# Zips -> Two
# Pockets -> Three


# Here:
# Blueprint -> Class
# Reebok Bag -> Object
# Campus Bag -> Object



# =========================================================
# WHAT IS AN OBJECT?
# =========================================================

# Object is an instance of a class.

# Class defines structure.
# Object uses that structure.



# =========================================================
# CREATING A CLASS
# =========================================================

class Bag:

    pass


# Creating Object

obj = Bag()

print(obj)

# Output:
# <__main__.Bag object at ...>



# =========================================================
# HOW TO CREATE OBJECT?
# =========================================================

# To create object:
# Call class inside variable.

# Syntax:
# variable = ClassName()


class Student:

    pass


student1 = Student()

print(student1)

# Output:
# <__main__.Student object at ...>



# =========================================================
# OBJECT WITH ATTRIBUTES
# =========================================================

class Bag:

    material = "Leather"
    zips = 3
    pockets = 4


# Creating Object

reebok = Bag()

print(reebok.material)
print(reebok.zips)
print(reebok.pockets)

# Output:
# Leather
# 3
# 4



# =========================================================
# MULTIPLE OBJECTS
# =========================================================

class Bag:

    brand = "Nike"


# Creating Multiple Objects

bag1 = Bag()
bag2 = Bag()

print(bag1.brand)
print(bag2.brand)

# Output:
# Nike
# Nike



# =========================================================
# OBJECTS WITH DIFFERENT VALUES
# =========================================================

# Constructor helps assign different values.

class Bag:

    def __init__(self, brand, material, zips, pockets):

        self.brand = brand
        self.material = material
        self.zips = zips
        self.pockets = pockets



# Creating Objects

reebok = Bag("Reebok", "Leather", 3, 4)

campus = Bag("Campus", "Leather", 2, 3)



# Accessing Object Data

print(reebok.brand)
print(reebok.material)
print(reebok.zips)
print(reebok.pockets)

# Output:
# Reebok
# Leather
# 3
# 4


print(campus.brand)
print(campus.material)
print(campus.zips)
print(campus.pockets)

# Output:
# Campus
# Leather
# 2
# 3



# =========================================================
# OBJECT METHODS
# =========================================================

# Objects can also use methods.

class Car:

    def start(self):

        print("Car Started")


# Creating Object

bmw = Car()

# Calling Method

bmw.start()

# Output:
# Car Started



# =========================================================
# OBJECT + ATTRIBUTE + METHOD
# =========================================================

class Student:

    def __init__(self, name):

        self.name = name


    def greet(self):

        print(f"Welcome {self.name}")


# Creating Object

student1 = Student("Ruchit")

# Calling Method

student1.greet()

# Output:
# Welcome Ruchit



# =========================================================
# MEMORY CONCEPT
# =========================================================

# Every object gets separate memory location.

class Demo:

    pass


obj1 = Demo()
obj2 = Demo()

print(obj1)
print(obj2)

# Output:
# Different memory addresses



# =========================================================
# MODIFYING OBJECT ATTRIBUTES
# =========================================================

class Student:

    def __init__(self, name):

        self.name = name


student1 = Student("Ruchit")

print(student1.name)

# Output:
# Ruchit


# Modifying Value

student1.name = "Rahul"

print(student1.name)

# Output:
# Rahul



# =========================================================
# OBJECTS ARE INDEPENDENT
# =========================================================

class Student:

    def __init__(self, name):

        self.name = name


student1 = Student("Ruchit")
student2 = Student("Rahul")

print(student1.name)
print(student2.name)

# Output:
# Ruchit
# Rahul


# Changing student1 value

student1.name = "Aman"

print(student1.name)
print(student2.name)

# Output:
# Aman
# Rahul


# Explanation:
# Objects store separate data.



# =========================================================
# CLASS VS OBJECT
# =========================================================

# CLASS
# - Blueprint
# - Template
# - Defines structure

# OBJECT
# - Real implementation
# - Created using class
# - Stores actual values



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Object is instance of class.
# 2. Objects are created using class blueprint.
# 3. Class is called inside variable to create object.
# 4. Every object gets separate memory.
# 5. Objects can access attributes and methods.
# 6. Constructor helps initialize object values.
# 7. Objects are independent from each other.



# =========================================================
# END OF OBJECTS IN PYTHON
# =========================================================



# =========================================================
# WHAT IS CONSTRUCTOR IN PYTHON?
# =========================================================

# For beginners:
# Think of Constructor like a function.

# Functions accept parameters.

# Similarly:
# Constructor allows class to accept values
# while creating objects.



# =========================================================
# WHAT IS A CONSTRUCTOR?
# =========================================================

# A Constructor is a special method
# that runs automatically whenever
# object is created.

# Constructor name in Python:
# __init__()

# __init__ is also called:
# Dunder Init Method



# =========================================================
# REAL LIFE EXAMPLE
# =========================================================

# BAG FACTORY

# Factory provides blueprint.

# Different companies provide requirements.

# Reebok:
# Material -> Leather
# Zips -> 3

# Campus:
# Material -> Leather
# Zips -> 2


# Constructor helps store different values
# for different objects automatically.



# =========================================================
# BASIC CONSTRUCTOR
# =========================================================

class Student:

    def __init__(self):

        print("Constructor Executed")


# Creating Object

obj = Student()

# Output:
# Constructor Executed


# Explanation:
# Constructor runs automatically
# when object is created.



# =========================================================
# CONSTRUCTOR WITH PARAMETERS
# =========================================================

class Student:

    def __init__(self, name):

        print(f"Welcome {name}")


# Creating Object

obj = Student("Ruchit")

# Output:
# Welcome Ruchit



# =========================================================
# SELF KEYWORD
# =========================================================

# Constructor targets current object location.

# To store current object reference,
# we use self keyword.

# self represents current object.



# =========================================================
# WHY SELF IS IMPORTANT?
# =========================================================

# self helps:
# - Store object data
# - Access object attributes
# - Access methods


# Without self:
# Values will not belong to object.



# =========================================================
# USING self TO STORE VALUES
# =========================================================

class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


# Creating Object

obj = Student("Ruchit", 20)

print(obj.name)
print(obj.age)

# Output:
# Ruchit
# 20



# =========================================================
# HOW self WORKS
# =========================================================

# self.name = name

# Left Side:
# Object Attribute

# Right Side:
# Parameter Value


# Example:
# self.name = "Ruchit"

# Means:
# Store "Ruchit" inside current object.



# =========================================================
# MULTIPLE OBJECTS WITH CONSTRUCTOR
# =========================================================

class Bag:

    def __init__(self, brand, material, zips):

        self.brand = brand
        self.material = material
        self.zips = zips


# Creating Objects

reebok = Bag("Reebok", "Leather", 3)

campus = Bag("Campus", "Leather", 2)



# Accessing Reebok Object

print(reebok.brand)
print(reebok.material)
print(reebok.zips)

# Output:
# Reebok
# Leather
# 3



# Accessing Campus Object

print(campus.brand)
print(campus.material)
print(campus.zips)

# Output:
# Campus
# Leather
# 2



# =========================================================
# OBJECTS STORE DIFFERENT VALUES
# =========================================================

# Constructor helps each object
# store separate values.

class Car:

    def __init__(self, brand, price):

        self.brand = brand
        self.price = price


car1 = Car("BMW", 5000000)
car2 = Car("Audi", 6000000)

print(car1.brand)
print(car1.price)

# Output:
# BMW
# 5000000


print(car2.brand)
print(car2.price)

# Output:
# Audi
# 6000000



# =========================================================
# CONSTRUCTOR + METHOD
# =========================================================

class Student:

    def __init__(self, name):

        self.name = name


    def greet(self):

        print(f"Hello {self.name}")


# Creating Object

obj = Student("Ruchit")

# Calling Method

obj.greet()

# Output:
# Hello Ruchit



# =========================================================
# DEFAULT CONSTRUCTOR
# =========================================================

# Python provides default constructor
# if we do not create one.

class Demo:

    pass


obj = Demo()

print(obj)

# Output:
# <__main__.Demo object at ...>



# =========================================================
# PARAMETERIZED CONSTRUCTOR
# =========================================================

# Constructor accepting values
# is called Parameterized Constructor.

class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary


emp = Employee("Ruchit", 50000)

print(emp.name)
print(emp.salary)

# Output:
# Ruchit
# 50000



# =========================================================
# MEMORY CONCEPT
# =========================================================

# Every object gets separate memory.

class Demo:

    def __init__(self):

        print("Object Created")


obj1 = Demo()
obj2 = Demo()

# Output:
# Object Created
# Object Created



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Constructor runs automatically.
# 2. Constructor name is __init__().
# 3. Constructor initializes object values.
# 4. self represents current object.
# 5. self stores object attributes.
# 6. Each object stores separate data.
# 7. Constructor can accept parameters.
# 8. Constructor simplifies object creation.



# =========================================================
# END OF CONSTRUCTOR IN PYTHON
# =========================================================


# =========================================================
# IN DEPTH ATTRIBUTES AND METHODS IN PYTHON
# =========================================================

# In Python OOPs:
# Attributes and Methods are very important concepts.

# Attributes -> Variables inside class
# Methods -> Functions inside class



# =========================================================
# TYPES OF ATTRIBUTES
# =========================================================

# 1. Instance Attribute
# 2. Class Attribute



# =========================================================
# INSTANCE ATTRIBUTE
# =========================================================

# Instance attributes are created using self keyword.

# Example:
# self.name
# self.age

# These attributes belong to object individually.


class Student:

    def __init__(self, name, age):

        self.name = name
        self.age = age


# Creating Objects

student1 = Student("Ruchit", 20)
student2 = Student("Rahul", 22)


print(student1.name)
print(student1.age)

# Output:
# Ruchit
# 20


print(student2.name)
print(student2.age)

# Output:
# Rahul
# 22



# =========================================================
# EACH OBJECT STORES SEPARATE DATA
# =========================================================

# Instance attributes are independent.

student1.name = "Aman"

print(student1.name)
print(student2.name)

# Output:
# Aman
# Rahul


# Explanation:
# Changing one object does not affect others.



# =========================================================
# CLASS ATTRIBUTE
# =========================================================

# Class attributes are created
# directly inside class
# without self keyword.

# Class attributes are shared by all objects.


class Student:

    college = "ABC College"


# Creating Objects

student1 = Student()
student2 = Student()


print(student1.college)
print(student2.college)

# Output:
# ABC College
# ABC College



# =========================================================
# CHANGING CLASS ATTRIBUTE
# =========================================================

Student.college = "XYZ College"

print(student1.college)
print(student2.college)

# Output:
# XYZ College
# XYZ College


# Explanation:
# Class attribute changes for all objects.



# =========================================================
# INSTANCE ATTRIBUTE VS CLASS ATTRIBUTE
# =========================================================

# INSTANCE ATTRIBUTE
# - Created using self
# - Separate for every object
# - Stored individually

# CLASS ATTRIBUTE
# - Created directly inside class
# - Shared among all objects
# - Same for all objects



# =========================================================
# TYPES OF METHODS
# =========================================================

# 1. Instance Method
# 2. Class Method
# 3. Static Method



# =========================================================
# INSTANCE METHOD
# =========================================================

# Instance methods use self parameter.

# They work with object-specific data.


class Student:

    def __init__(self, name):

        self.name = name


    def greet(self):

        print(f"Hello {self.name}")


# Creating Object

obj = Student("Ruchit")

obj.greet()

# Output:
# Hello Ruchit



# =========================================================
# CLASS METHOD
# =========================================================

# Class methods use @classmethod decorator.

# They use cls parameter instead of self.

# cls refers to class itself.


class Student:

    college = "ABC College"


    @classmethod
    def show_college(cls):

        print(cls.college)


# Calling Class Method

Student.show_college()

# Output:
# ABC College



# =========================================================
# CLASS METHOD MODIFYING CLASS ATTRIBUTE
# =========================================================

class Student:

    college = "ABC College"


    @classmethod
    def change_college(cls, new_college):

        cls.college = new_college


Student.change_college("XYZ College")

print(Student.college)

# Output:
# XYZ College



# =========================================================
# STATIC METHOD
# =========================================================

# Static methods do not depend
# on object or class.

# They do NOT use:
# - self
# - cls

# Static method uses @staticmethod decorator.


class Math:

    @staticmethod
    def addition(a, b):

        print(a + b)


# Calling Static Method

Math.addition(10, 20)

# Output:
# 30



# =========================================================
# STATIC METHOD EXAMPLE
# =========================================================

class Temperature:

    @staticmethod
    def celsius_to_fahrenheit(celsius):

        return (celsius * 9/5) + 32


print(Temperature.celsius_to_fahrenheit(30))

# Output:
# 86.0



# =========================================================
# COMPARING ALL METHODS
# =========================================================

class Demo:

    # Class Attribute
    company = "OpenAI"


    # Constructor
    def __init__(self, name):

        # Instance Attribute
        self.name = name


    # Instance Method
    def show_name(self):

        print(self.name)


    # Class Method
    @classmethod
    def show_company(cls):

        print(cls.company)


    # Static Method
    @staticmethod
    def add(a, b):

        print(a + b)



# Creating Object

obj = Demo("Ruchit")


# Calling Instance Method
obj.show_name()

# Output:
# Ruchit


# Calling Class Method
Demo.show_company()

# Output:
# OpenAI


# Calling Static Method
Demo.add(5, 5)

# Output:
# 10



# =========================================================
# MEMORY UNDERSTANDING
# =========================================================

# Instance Attribute:
# Stored separately for every object.

# Class Attribute:
# Shared memory among objects.



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Attributes are variables inside class.
# 2. Methods are functions inside class.
# 3. Instance attributes use self keyword.
# 4. Class attributes are shared.
# 5. Instance methods use self parameter.
# 6. Class methods use cls parameter.
# 7. Static methods use neither self nor cls.
# 8. @classmethod creates class method.
# 9. @staticmethod creates static method.
# 10. Instance methods work on object data.



# =========================================================
# END OF ATTRIBUTES AND METHODS
# =========================================================


# =========================================================
# INHERITANCE IN PYTHON
# =========================================================

# Inheritance is a mechanism
# by which one class (Child Class)
# can use properties and methods
# of another class (Parent Class).

# Parent Class is also called:
# - Base Class
# - Super Class

# Child Class is also called:
# - Derived Class
# - Sub Class



# =========================================================
# WHY INHERITANCE?
# =========================================================

# Inheritance helps:
# - Reuse code
# - Reduce repetition
# - Improve maintainability



# =========================================================
# REAL LIFE EXAMPLE
# =========================================================

# Parent:
# Animal

# Child:
# Dog
# Cat

# Dog and Cat can use
# common Animal properties.



# =========================================================
# SINGLE LEVEL INHERITANCE
# =========================================================

# One class inherits from another class.

# Parent Class -> Child Class



# =========================================================
# SINGLE LEVEL EXAMPLE
# =========================================================

class Parent:

    def show(self):

        print("Parent Class Method")


class Child(Parent):

    pass


# Creating Object

obj = Child()

obj.show()

# Output:
# Parent Class Method


# Explanation:
# Child class inherited Parent method.



# =========================================================
# SINGLE LEVEL WITH ATTRIBUTES
# =========================================================

class Animal:

    def __init__(self):

        self.type = "Mammal"


class Dog(Animal):

    def bark(self):

        print("Dog Barks")


obj = Dog()

print(obj.type)

# Output:
# Mammal


obj.bark()

# Output:
# Dog Barks



# =========================================================
# MULTILEVEL INHERITANCE
# =========================================================

# A class inherits from another child class.

# GrandParent -> Parent -> Child



# =========================================================
# MULTILEVEL EXAMPLE
# =========================================================

class GrandParent:

    def grandparent_method(self):

        print("Grand Parent Method")


class Parent(GrandParent):

    def parent_method(self):

        print("Parent Method")


class Child(Parent):

    def child_method(self):

        print("Child Method")


# Creating Object

obj = Child()

obj.grandparent_method()
obj.parent_method()
obj.child_method()

# Output:
# Grand Parent Method
# Parent Method
# Child Method



# =========================================================
# MULTIPLE INHERITANCE
# =========================================================

# One child inherits from multiple parents.

# Parent1
# Parent2
#    ↓
#   Child



# =========================================================
# MULTIPLE INHERITANCE EXAMPLE
# =========================================================

class Father:

    def father_quality(self):

        print("Father Quality")


class Mother:

    def mother_quality(self):

        print("Mother Quality")


class Child(Father, Mother):

    pass


obj = Child()

obj.father_quality()
obj.mother_quality()

# Output:
# Father Quality
# Mother Quality



# =========================================================
# HIERARCHICAL INHERITANCE
# =========================================================

# Multiple child classes inherit
# from single parent class.

#        Parent
#       /     \
#   Child1   Child2



# =========================================================
# HIERARCHICAL EXAMPLE
# =========================================================

class Parent:

    def display(self):

        print("Parent Method")


class Child1(Parent):

    pass


class Child2(Parent):

    pass


obj1 = Child1()
obj2 = Child2()

obj1.display()
obj2.display()

# Output:
# Parent Method
# Parent Method



# =========================================================
# USING super() FUNCTION
# =========================================================

# super() accesses Parent class methods.

class Parent:

    def __init__(self):

        print("Parent Constructor")


class Child(Parent):

    def __init__(self):

        super().__init__()

        print("Child Constructor")


obj = Child()

# Output:
# Parent Constructor
# Child Constructor



# =========================================================
# METHOD OVERRIDING
# =========================================================

# Child class can modify Parent method.

class Parent:

    def show(self):

        print("Parent Method")


class Child(Parent):

    def show(self):

        print("Child Method")


obj = Child()

obj.show()

# Output:
# Child Method



# =========================================================
# ACCESSING PARENT METHOD INSIDE CHILD
# =========================================================

class Parent:

    def display(self):

        print("Parent Display")


class Child(Parent):

    def display(self):

        super().display()

        print("Child Display")


obj = Child()

obj.display()

# Output:
# Parent Display
# Child Display



# =========================================================
# isinstance() FUNCTION
# =========================================================

# Checks object belongs to class or not.

class Animal:

    pass


class Dog(Animal):

    pass


obj = Dog()

print(isinstance(obj, Dog))

# Output:
# True


print(isinstance(obj, Animal))

# Output:
# True



# =========================================================
# issubclass() FUNCTION
# =========================================================

# Checks inheritance relationship.

class Parent:

    pass


class Child(Parent):

    pass


print(issubclass(Child, Parent))

# Output:
# True



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Inheritance allows code reuse.
# 2. Child class inherits Parent properties.
# 3. Single Level -> One Parent One Child.
# 4. Multilevel -> Chain of inheritance.
# 5. Multiple -> Multiple Parents One Child.
# 6. Hierarchical -> One Parent Multiple Children.
# 7. super() accesses Parent class methods.
# 8. Method overriding changes Parent behavior.
# 9. isinstance() checks object type.
# 10. issubclass() checks class relationship.



# =========================================================
# END OF INHERITANCE
# =========================================================


# =========================================================
# ENCAPSULATION IN PYTHON
# =========================================================

# Encapsulation means:
# Bundling data (attributes)
# and methods into one unit (class).

# It also means:
# Controlling access to data
# using Access Modifiers.



# =========================================================
# WHY ENCAPSULATION?
# =========================================================

# Encapsulation helps:
# - Protect data
# - Prevent accidental changes
# - Increase security
# - Improve code organization



# =========================================================
# ACCESS MODIFIERS
# =========================================================

# Python has mainly 3 access modifiers:

# 1. Public
# 2. Protected
# 3. Private



# =========================================================
# PUBLIC MEMBERS
# =========================================================

# Public members are accessible everywhere.

# Until now we were mostly using
# public attributes and methods.


class Student:

    def __init__(self):

        self.name = "Ruchit"


    def display(self):

        print("Public Method")


# Creating Object

obj = Student()


# Accessing Public Attribute

print(obj.name)

# Output:
# Ruchit


# Accessing Public Method

obj.display()

# Output:
# Public Method



# =========================================================
# PROTECTED MEMBERS
# =========================================================

# Protected members use single underscore (_)

# Protected members should only be accessed:
# - Inside class
# - Inside child classes

# NOTE:
# Python does not enforce protection strictly
# like Java or C++.


class Student:

    def __init__(self):

        self._age = 20


    def _show(self):

        print("Protected Method")


obj = Student()

print(obj._age)

# Output:
# 20


obj._show()

# Output:
# Protected Method


# NOTE:
# Technically accessible outside class,
# but should be treated as protected.



# =========================================================
# PROTECTED MEMBERS IN INHERITANCE
# =========================================================

class Parent:

    def __init__(self):

        self._money = 50000


class Child(Parent):

    def display(self):

        print(self._money)


obj = Child()

obj.display()

# Output:
# 50000


# Explanation:
# Protected members are accessible
# inside child classes.



# =========================================================
# PRIVATE MEMBERS
# =========================================================

# Private members use double underscore (__)

# Private means:
# Accessible only inside same class.

# Not directly accessible outside class.
# Not directly accessible in child class.


class Student:

    def __init__(self):

        self.__salary = 50000


    def __private_method(self):

        print("Private Method")


    def access_private(self):

        print(self.__salary)

        self.__private_method()


obj = Student()


# Accessing through public method

obj.access_private()

# Output:
# 50000
# Private Method



# =========================================================
# DIRECT ACCESS OF PRIVATE MEMBERS
# =========================================================

class Student:

    def __init__(self):

        self.__salary = 50000


obj = Student()

# print(obj.__salary)

# Output:
# AttributeError


# Explanation:
# Private attributes cannot be accessed directly.



# =========================================================
# NAME MANGLING
# =========================================================

# Python internally changes private names.

class Student:

    def __init__(self):

        self.__salary = 50000


obj = Student()

print(obj._Student__salary)

# Output:
# 50000


# NOTE:
# This is called Name Mangling.

# Technically possible,
# but should not be used normally.



# =========================================================
# PRIVATE MEMBERS IN CHILD CLASS
# =========================================================

class Parent:

    def __init__(self):

        self.__money = 100000


class Child(Parent):

    def display(self):

        # print(self.__money)

        print("Cannot Access Private Attribute Directly")


obj = Child()

obj.display()

# Output:
# Cannot Access Private Attribute Directly


# Explanation:
# Private members are NOT inherited directly.



# =========================================================
# ENCAPSULATION EXAMPLE
# =========================================================

class BankAccount:

    def __init__(self, balance):

        self.__balance = balance


    def deposit(self, amount):

        self.__balance += amount

        print(f"Deposited : {amount}")


    def withdraw(self, amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print(f"Withdrawn : {amount}")

        else:

            print("Insufficient Balance")


    def show_balance(self):

        print(f"Current Balance : {self.__balance}")


# Creating Object

account = BankAccount(1000)


account.deposit(500)

# Output:
# Deposited : 500


account.withdraw(200)

# Output:
# Withdrawn : 200


account.show_balance()

# Output:
# Current Balance : 1300


# Direct access not allowed

# print(account.__balance)

# Output:
# AttributeError



# =========================================================
# GETTER METHOD
# =========================================================

# Getter method reads private data.

class Student:

    def __init__(self):

        self.__marks = 90


    def get_marks(self):

        return self.__marks


obj = Student()

print(obj.get_marks())

# Output:
# 90



# =========================================================
# SETTER METHOD
# =========================================================

# Setter method modifies private data safely.

class Student:

    def __init__(self):

        self.__marks = 0


    def set_marks(self, marks):

        if marks >= 0 and marks <= 100:

            self.__marks = marks

        else:

            print("Invalid Marks")


    def get_marks(self):

        return self.__marks


obj = Student()

obj.set_marks(95)

print(obj.get_marks())

# Output:
# 95



# =========================================================
# PUBLIC VS PROTECTED VS PRIVATE
# =========================================================

# PUBLIC
# - Accessible everywhere
# - No underscore

# PROTECTED
# - Single underscore (_)
# - Accessible in class and subclasses

# PRIVATE
# - Double underscore (__)
# - Accessible only inside class



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Encapsulation bundles data and methods.
# 2. Encapsulation provides security.
# 3. Public members are accessible everywhere.
# 4. Protected members use single underscore (_).
# 5. Private members use double underscore (__).
# 6. Private members cannot be directly accessed.
# 7. Getter methods read private data.
# 8. Setter methods modify private data safely.
# 9. Encapsulation prevents accidental modification.
# 10. Name Mangling changes private variable names internally.



# =========================================================
# END OF ENCAPSULATION
# =========================================================


# =========================================================
# POLYMORPHISM IN PYTHON
# =========================================================

# Poly means Many
# Morphism means Forms

# Polymorphism means:
# One thing having many forms.


# In Python:
# Different classes can have methods
# with same name but different behavior.



# =========================================================
# WHY POLYMORPHISM?
# =========================================================

# Polymorphism helps:
# - Increase flexibility
# - Reduce complexity
# - Improve code reusability



# =========================================================
# REAL LIFE EXAMPLE
# =========================================================

# Example:
# Animal Sound

# Dog -> Bark
# Cat -> Meow
# Cow -> Moo

# Same method:
# sound()

# Different behavior for each class.



# =========================================================
# BASIC POLYMORPHISM
# =========================================================

class Dog:

    def sound(self):

        print("Dog Barks")


class Cat:

    def sound(self):

        print("Cat Meows")


class Cow:

    def sound(self):

        print("Cow Moos")


# Creating Objects

dog = Dog()
cat = Cat()
cow = Cow()


dog.sound()

# Output:
# Dog Barks


cat.sound()

# Output:
# Cat Meows


cow.sound()

# Output:
# Cow Moos



# =========================================================
# SAME METHOD DIFFERENT BEHAVIOR
# =========================================================

# This is polymorphism.

animals = [Dog(), Cat(), Cow()]

for animal in animals:

    animal.sound()

# Output:
# Dog Barks
# Cat Meows
# Cow Moos



# =========================================================
# TYPES OF POLYMORPHISM
# =========================================================

# 1. Method Overloading
# 2. Method Overriding



# =========================================================
# METHOD OVERLOADING
# =========================================================

# Python does not support traditional
# method overloading directly.

# But Python simulates overloading using:
# - Default arguments
# - Variable length arguments



# =========================================================
# METHOD OVERLOADING USING DEFAULT ARGUMENT
# =========================================================

class Addition:

    def add(self, a, b=0, c=0):

        print(a + b + c)


obj = Addition()

obj.add(10, 20)

# Output:
# 30


obj.add(10, 20, 30)

# Output:
# 60


# Explanation:
# Same method works with different arguments.



# =========================================================
# METHOD OVERLOADING USING *args
# =========================================================

class Calculator:

    def addition(self, *numbers):

        total = 0

        for num in numbers:

            total += num

        print(total)


obj = Calculator()

obj.addition(10, 20)

# Output:
# 30


obj.addition(10, 20, 30, 40)

# Output:
# 100



# =========================================================
# METHOD OVERRIDING
# =========================================================

# Method overriding occurs when:
# Child class defines method
# with same name as Parent class.


# Child method replaces Parent method.



# =========================================================
# METHOD OVERRIDING EXAMPLE
# =========================================================

class Parent:

    def show(self):

        print("Parent Method")


class Child(Parent):

    def show(self):

        print("Child Method")


obj = Child()

obj.show()

# Output:
# Child Method


# Explanation:
# Child method overrides Parent method.



# =========================================================
# ACCESSING PARENT METHOD USING super()
# =========================================================

class Parent:

    def display(self):

        print("Parent Display")


class Child(Parent):

    def display(self):

        super().display()

        print("Child Display")


obj = Child()

obj.display()

# Output:
# Parent Display
# Child Display



# =========================================================
# REAL LIFE OVERRIDING EXAMPLE
# =========================================================

class Vehicle:

    def start(self):

        print("Vehicle Started")


class Car(Vehicle):

    def start(self):

        print("Car Started")


class Bike(Vehicle):

    def start(self):

        print("Bike Started")


car = Car()
bike = Bike()

car.start()

# Output:
# Car Started


bike.start()

# Output:
# Bike Started



# =========================================================
# POLYMORPHISM WITH BUILT-IN FUNCTIONS
# =========================================================

# Same len() function behaves differently.

print(len("Ruchit"))

# Output:
# 6


print(len([10, 20, 30]))

# Output:
# 3


print(len((1, 2, 3, 4)))

# Output:
# 4


# Explanation:
# Same function works differently
# for different data types.



# =========================================================
# OPERATOR POLYMORPHISM
# =========================================================

# + operator behaves differently.

print(10 + 20)

# Output:
# 30


print("Hello " + "Ruchit")

# Output:
# Hello Ruchit


print([1, 2] + [3, 4])

# Output:
# [1, 2, 3, 4]


# Explanation:
# Same operator behaves differently.



# =========================================================
# POLYMORPHISM USING FUNCTIONS
# =========================================================

class Dog:

    def sound(self):

        print("Dog Barks")


class Cat:

    def sound(self):

        print("Cat Meows")


def animal_sound(animal):

    animal.sound()


dog = Dog()
cat = Cat()

animal_sound(dog)

# Output:
# Dog Barks


animal_sound(cat)

# Output:
# Cat Meows



# =========================================================
# ADVANTAGES OF POLYMORPHISM
# =========================================================

# 1. Code Reusability
# 2. Flexibility
# 3. Easy Maintenance
# 4. Cleaner Code
# 5. Extensibility



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Polymorphism means many forms.
# 2. Same method can behave differently.
# 3. Method Overloading uses default/*args.
# 4. Python does not support traditional overloading.
# 5. Method Overriding replaces Parent method.
# 6. super() accesses Parent method.
# 7. Polymorphism improves flexibility.
# 8. Built-in functions also show polymorphism.
# 9. Operators can behave polymorphically.



# =========================================================
# END OF POLYMORPHISM
# =========================================================



# =========================================================
# ABSTRACTION IN PYTHON
# =========================================================

# Abstraction means:
# Hiding unnecessary details
# and showing only essential features.

# It simplifies complex systems.



# =========================================================
# REAL LIFE EXAMPLE
# =========================================================

# Example:
# Car

# User only knows:
# - Start Car
# - Stop Car
# - Drive Car

# User does NOT know:
# - Engine Internal Working
# - Fuel Injection Process
# - Gearbox Mechanics

# Hidden implementation = Abstraction



# =========================================================
# WHY ABSTRACTION?
# =========================================================

# Abstraction helps:
# - Reduce complexity
# - Increase security
# - Hide internal implementation
# - Focus on important features



# =========================================================
# ABSTRACT CLASS
# =========================================================

# Abstract Class:
# A class containing one or more
# abstract methods.

# Abstract class cannot create objects directly.



# =========================================================
# ABSTRACT METHOD
# =========================================================

# Abstract Method:
# Method declared but NOT implemented.

# Child classes MUST implement it.



# =========================================================
# abc MODULE
# =========================================================

# Python uses abc module
# to create abstraction.

# abc = Abstract Base Class

from abc import ABC, abstractmethod



# =========================================================
# CREATING ABSTRACT CLASS
# =========================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass


# Explanation:
# Vehicle is abstract class.
# start() is abstract method.



# =========================================================
# CANNOT CREATE OBJECT OF ABSTRACT CLASS
# =========================================================

# obj = Vehicle()

# Output:
# TypeError:
# Can't instantiate abstract class



# =========================================================
# IMPLEMENTING ABSTRACT METHOD
# =========================================================

class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass



class Car(Vehicle):

    def start(self):

        print("Car Started")


# Creating Object

obj = Car()

obj.start()

# Output:
# Car Started



# =========================================================
# MULTIPLE CHILD CLASSES
# =========================================================

class Animal(ABC):

    @abstractmethod
    def sound(self):

        pass



class Dog(Animal):

    def sound(self):

        print("Dog Barks")



class Cat(Animal):

    def sound(self):

        print("Cat Meows")



dog = Dog()
cat = Cat()

dog.sound()

# Output:
# Dog Barks


cat.sound()

# Output:
# Cat Meows



# =========================================================
# ABSTRACT CLASS WITH NORMAL METHODS
# =========================================================

# Abstract class can contain:
# - Abstract methods
# - Normal methods


class Vehicle(ABC):

    @abstractmethod
    def start(self):

        pass


    def stop(self):

        print("Vehicle Stopped")



class Bike(Vehicle):

    def start(self):

        print("Bike Started")


obj = Bike()

obj.start()

# Output:
# Bike Started


obj.stop()

# Output:
# Vehicle Stopped



# =========================================================
# ABSTRACT CLASS WITH CONSTRUCTOR
# =========================================================

class Person(ABC):

    def __init__(self, name):

        self.name = name


    @abstractmethod
    def profession(self):

        pass



class Doctor(Person):

    def profession(self):

        print(f"{self.name} is a Doctor")


obj = Doctor("Ruchit")

obj.profession()

# Output:
# Ruchit is a Doctor



# =========================================================
# REAL LIFE PAYMENT EXAMPLE
# =========================================================

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):

        pass



class CreditCard(Payment):

    def pay(self, amount):

        print(f"Paid {amount} using Credit Card")



class UPI(Payment):

    def pay(self, amount):

        print(f"Paid {amount} using UPI")



credit = CreditCard()
upi = UPI()

credit.pay(500)

# Output:
# Paid 500 using Credit Card


upi.pay(1000)

# Output:
# Paid 1000 using UPI



# =========================================================
# ADVANTAGES OF ABSTRACTION
# =========================================================

# 1. Reduces complexity
# 2. Hides unnecessary details
# 3. Improves security
# 4. Improves maintainability
# 5. Forces child classes to implement methods



# =========================================================
# DIFFERENCE BETWEEN ABSTRACTION
# AND ENCAPSULATION
# =========================================================

# ABSTRACTION
# - Hides implementation details
# - Focuses on "What"

# ENCAPSULATION
# - Hides data
# - Focuses on "How"



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Abstraction hides unnecessary details.
# 2. Abstract class contains abstract methods.
# 3. Abstract methods have declaration only.
# 4. Child classes must implement abstract methods.
# 5. abc module is used for abstraction.
# 6. ABC class creates abstract base class.
# 7. @abstractmethod creates abstract method.
# 8. Objects of abstract class cannot be created.
# 9. Abstract class can contain normal methods too.



# =========================================================
# END OF ABSTRACTION
# =========================================================


# =========================================================
# DUNDER / MAGIC METHODS IN PYTHON
# =========================================================

# Dunder means:
# Double Underscore

# Magic Methods are special methods
# used to define object behavior
# for built-in operations.

# Examples:
# __init__
# __str__
# __len__

# These methods are automatically called
# by Python in different situations.



# =========================================================
# WHY DUNDER METHODS?
# =========================================================

# Dunder methods help objects behave like:
# - Numbers
# - Lists
# - Strings
# - Dictionaries

# They provide operator overloading
# and built-in functionality.



# =========================================================
# __init__ METHOD
# =========================================================

# Constructor method.

# Automatically runs
# when object is created.


class Student:

    def __init__(self, name):

        self.name = name

        print("Constructor Called")


obj = Student("Ruchit")

# Output:
# Constructor Called



# =========================================================
# __str__ METHOD
# =========================================================

# Defines string representation of object.

# Without __str__

class Student:

    def __init__(self, name):

        self.name = name


obj = Student("Ruchit")

print(obj)

# Output:
# <__main__.Student object at ...>


# With __str__

class Student:

    def __init__(self, name):

        self.name = name


    def __str__(self):

        return f"Student Name : {self.name}"


obj = Student("Ruchit")

print(obj)

# Output:
# Student Name : Ruchit



# =========================================================
# __len__ METHOD
# =========================================================

# Defines behavior of len() function.

class Book:

    def __len__(self):

        return 500


obj = Book()

print(len(obj))

# Output:
# 500



# =========================================================
# __add__ METHOD
# =========================================================

# Defines behavior of + operator.

class Number:

    def __init__(self, value):

        self.value = value


    def __add__(self, other):

        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print(num1 + num2)

# Output:
# 30



# =========================================================
# __eq__ METHOD
# =========================================================

# Defines behavior of == operator.

class Student:

    def __init__(self, marks):

        self.marks = marks


    def __eq__(self, other):

        return self.marks == other.marks


student1 = Student(90)
student2 = Student(90)

print(student1 == student2)

# Output:
# True



# =========================================================
# __getitem__ METHOD
# =========================================================

# Allows indexing like list or dictionary.

class MyList:

    def __init__(self, data):

        self.data = data


    def __getitem__(self, index):

        return self.data[index]


obj = MyList([10, 20, 30, 40])

print(obj[0])

# Output:
# 10


print(obj[2])

# Output:
# 30



# =========================================================
# __setitem__ METHOD
# =========================================================

# Allows assigning values using indexing.

class MyList:

    def __init__(self, data):

        self.data = data


    def __setitem__(self, index, value):

        self.data[index] = value


obj = MyList([10, 20, 30])

obj[1] = 100

print(obj.data)

# Output:
# [10, 100, 30]



# =========================================================
# __delitem__ METHOD
# =========================================================

# Allows deleting values using del keyword.

class MyList:

    def __init__(self, data):

        self.data = data


    def __delitem__(self, index):

        del self.data[index]


obj = MyList([10, 20, 30])

del obj[1]

print(obj.data)

# Output:
# [10, 30]



# =========================================================
# __contains__ METHOD
# =========================================================

# Defines behavior of 'in' operator.

class MyList:

    def __init__(self, data):

        self.data = data


    def __contains__(self, item):

        return item in self.data


obj = MyList([10, 20, 30])

print(20 in obj)

# Output:
# True



# =========================================================
# __call__ METHOD
# =========================================================

# Makes object callable like function.

class Demo:

    def __call__(self):

        print("Object Called Like Function")


obj = Demo()

obj()

# Output:
# Object Called Like Function



# =========================================================
# __repr__ METHOD
# =========================================================

# Official string representation.

class Student:

    def __repr__(self):

        return "Student Object"


obj = Student()

print(obj)

# Output:
# Student Object



# =========================================================
# __lt__ METHOD
# =========================================================

# Defines behavior of < operator.

class Number:

    def __init__(self, value):

        self.value = value


    def __lt__(self, other):

        return self.value < other.value


num1 = Number(10)
num2 = Number(20)

print(num1 < num2)

# Output:
# True



# =========================================================
# __gt__ METHOD
# =========================================================

# Defines behavior of > operator.

class Number:

    def __init__(self, value):

        self.value = value


    def __gt__(self, other):

        return self.value > other.value


num1 = Number(50)
num2 = Number(20)

print(num1 > num2)

# Output:
# True



# =========================================================
# OPERATOR OVERLOADING
# =========================================================

# Dunder methods enable operator overloading.

class Vector:

    def __init__(self, x):

        self.x = x


    def __add__(self, other):

        return self.x + other.x


v1 = Vector(5)
v2 = Vector(10)

print(v1 + v2)

# Output:
# 15



# =========================================================
# BUILT-IN FUNCTIONS USING DUNDER METHODS
# =========================================================

# len()  -> __len__
# print() -> __str__
# + -> __add__
# == -> __eq__
# [] -> __getitem__



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Dunder means Double Underscore.
# 2. Magic methods define object behavior.
# 3. __init__ is constructor.
# 4. __str__ defines string representation.
# 5. __len__ works with len().
# 6. __add__ overloads + operator.
# 7. __eq__ overloads == operator.
# 8. __getitem__ enables indexing.
# 9. Dunder methods provide operator overloading.
# 10. Python automatically calls these methods.



# =========================================================
# END OF DUNDER / MAGIC METHODS
# =========================================================