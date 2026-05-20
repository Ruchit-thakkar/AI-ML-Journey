# =========================================
# PYTHON FUNCTIONS - COMPLETE NOTES
# =========================================


# =========================================
# 1. WHAT ARE FUNCTIONS?
# =========================================

# Functions are reusable blocks of code.
# They help us avoid writing the same code again and again.


# =========================================
# 2. IMPERATIVE CODE VS FUNCTIONAL CODE
# =========================================


# -----------------------------------------
# IMPERATIVE CODE
# -----------------------------------------

# Repeating same code manually

print("Hello Ruchit")
print("Hello Ruchit")
print("Hello Ruchit")

# Output:
# Hello Ruchit
# Hello Ruchit
# Hello Ruchit


# Problem:
# - Code repetition
# - Hard to manage
# - Bigger programs become messy



# -----------------------------------------
# FUNCTIONAL CODE
# -----------------------------------------

# Creating function once and reusing it

def greet():
    print("Hello Ruchit")


# Calling function multiple times
greet()
greet()
greet()

# Output:
# Hello Ruchit
# Hello Ruchit
# Hello Ruchit


# Advantages:
# - Reusable code
# - Cleaner code
# - Easier debugging
# - Better organization



# =========================================
# 3. SYNTAX OF FUNCTION
# =========================================

# Syntax:
#
# def function_name():
#     code


# Example

def welcome():
    print("Welcome to Python Functions")


# Function Call
welcome()

# Output:
# Welcome to Python Functions



# =========================================
# 4. CALLING A FUNCTION
# =========================================

# A function only runs when it is called.


def say_hello():
    print("Hello!")


# Calling the function
say_hello()

# Output:
# Hello!



# =========================================
# 5. PRINT VS RETURN
# =========================================


# -----------------------------------------
# USING PRINT
# -----------------------------------------

# print() only displays output on terminal


def add_using_print():
    print(10 + 20)


add_using_print()

# Output:
# 30



# -----------------------------------------
# USING RETURN
# -----------------------------------------

# return sends value back to where function was called


def add_using_return():
    return 10 + 20


result = add_using_return()

print(result)

# Output:
# 30



# -----------------------------------------
# DIFFERENCE BETWEEN PRINT AND RETURN
# -----------------------------------------

def using_print():
    print(5 + 5)


def using_return():
    return 5 + 5


a = using_print()
b = using_return()

print(a)
print(b)

# Output:
# 10
# None
# 10


# Explanation:
# using_print() only prints value
# so variable 'a' stores None

# using_return() returns value
# so variable 'b' stores 10



# =========================================
# 6. PARAMETERS AND ARGUMENTS
# =========================================

# Parameters:
# Variables accepted by function

# Arguments:
# Actual values passed to parameters


def greet_user(name):   # name = parameter
    print(f"Hello {name}")


greet_user("Ruchit")    # "Ruchit" = argument

# Output:
# Hello Ruchit



# =========================================
# 7. MULTIPLE PARAMETERS
# =========================================

def student_info(name, age):
    print(f"Name : {name}")
    print(f"Age  : {age}")


student_info("Ruchit", 20)

# Output:
# Name : Ruchit
# Age  : 20



# =========================================
# 8. DEFAULT PARAMETERS
# =========================================

# Default parameter means parameter already has value


def country(name="India"):
    print(f"Country : {name}")


country()

# Output:
# Country : India


country("Canada")

# Output:
# Country : Canada



# =========================================
# 9. KEYWORD ARGUMENTS
# =========================================

# Passing values using parameter names


def employee(name, salary):
    print(f"Name   : {name}")
    print(f"Salary : {salary}")


employee(salary=50000, name="Ruchit")

# Output:
# Name   : Ruchit
# Salary : 50000



# =========================================
# 10. POSITIONAL ARGUMENTS
# =========================================

# Values passed according to position


def numbers(a, b):
    print(a)
    print(b)


numbers(10, 20)

# Output:
# 10
# 20



# =========================================
# 11. ARBITRARY ARGUMENTS (*args)
# =========================================

# *args allows multiple values


def total_marks(*marks):
    print(marks)


total_marks(80, 90, 95, 70)

# Output:
# (80, 90, 95, 70)


# Explanation:
# *args stores values inside tuple



# =========================================
# 12. LOOPING THROUGH *args
# =========================================

def add_numbers(*numbers):
    total = 0

    for num in numbers:
        total += num

    print(f"Total = {total}")


add_numbers(10, 20, 30)

# Output:
# Total = 60



# =========================================
# 13. KEYWORD VARIABLE ARGUMENTS (**kwargs)
# =========================================

# **kwargs accepts multiple keyword arguments


def user_info(**details):
    print(details)


user_info(name="Ruchit", age=20, city="Ahmedabad")

# Output:
# {'name': 'Ruchit', 'age': 20, 'city': 'Ahmedabad'}


# Explanation:
# **kwargs stores data in dictionary



# =========================================
# 14. ACCESSING kwargs VALUES
# =========================================

def profile(**data):

    for key, value in data.items():
        print(f"{key} : {value}")


profile(name="Ruchit", profession="Developer", country="India")

# Output:
# name : Ruchit
# profession : Developer
# country : India



# =========================================
# 15. FUNCTION RETURNING MULTIPLE VALUES
# =========================================

def calculations(a, b):

    addition = a + b
    subtraction = a - b

    return addition, subtraction


add, sub = calculations(20, 10)

print("Addition :", add)
print("Subtraction :", sub)

# Output:
# Addition : 30
# Subtraction : 10



# =========================================
# 16. NESTED FUNCTION
# =========================================

# Function inside another function


def outer():

    print("Outer Function")

    def inner():
        print("Inner Function")

    inner()


outer()

# Output:
# Outer Function
# Inner Function



# =========================================
# 17. RECURSIVE FUNCTION
# =========================================

# Function calling itself


def countdown(n):

    if n == 0:
        print("Done")
        return

    print(n)

    countdown(n - 1)


countdown(5)

# Output:
# 5
# 4
# 3
# 2
# 1
# Done



# =========================================
# 18. LAMBDA FUNCTION
# =========================================

# Small anonymous function


square = lambda x: x * x

print(square(5))

# Output:
# 25



# =========================================
# 19. IMPORTANT POINTS
# =========================================

# 1. Functions make code reusable
# 2. def keyword is used to create function
# 3. Function runs only when called
# 4. return sends value back
# 5. print only displays output
# 6. Parameters are variables
# 7. Arguments are actual values
# 8. *args stores multiple positional arguments
# 9. **kwargs stores multiple keyword arguments
# 10. Functions improve readability and management


# =========================================================
# INTRODUCTION TO DATA STRUCTURES
# =========================================================

# Data Structures are a type of storage
# in which we can store multiple values.

# Example:
# Instead of storing one value at a time,
# data structures allow storing many values together.


# =========================================================
# NORMAL VARIABLE
# =========================================================

name1 = "Ruchit"
name2 = "Rahul"
name3 = "Aman"

print(name1)
print(name2)
print(name3)

# Output:
# Ruchit
# Rahul
# Aman


# Problem:
# Storing too many variables separately
# becomes difficult to manage.


# =========================================================
# USING DATA STRUCTURE
# =========================================================

names = ["Ruchit", "Rahul", "Aman"]

print(names)

# Output:
# ['Ruchit', 'Rahul', 'Aman']


# Here:
# Multiple values are stored inside one variable.



# =========================================================
# TYPES OF DATA STRUCTURES
# =========================================================

# 1. In-built Data Structures
# 2. Customized Data Structures



# =========================================================
# 1. IN-BUILT DATA STRUCTURES
# =========================================================

# Python already provides these data structures.

# List
# Tuple
# Dictionary
# Set


# =========================================================
# LIST
# =========================================================

# List stores multiple values.
# List is ordered and changeable (mutable).

fruits = ["Apple", "Banana", "Mango"]

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango']


# Accessing values using index
print(fruits[0])

# Output:
# Apple


# Changing value
fruits[1] = "Orange"

print(fruits)

# Output:
# ['Apple', 'Orange', 'Mango']



# =========================================================
# TUPLE
# =========================================================

# Tuple also stores multiple values.
# Tuple is ordered but NOT changeable (immutable).

colors = ("Red", "Green", "Blue")

print(colors)

# Output:
# ('Red', 'Green', 'Blue')


# Accessing values
print(colors[1])

# Output:
# Green


# colors[1] = "Yellow"
# Error because tuple cannot be modified.



# =========================================================
# DICTIONARY
# =========================================================

# Dictionary stores data in key-value pairs.

student = {
    "name": "Ruchit",
    "age": 20,
    "course": "AI/ML"
}

print(student)

# Output:
# {'name': 'Ruchit', 'age': 20, 'course': 'AI/ML'}


# Accessing values using keys
print(student["name"])

# Output:
# Ruchit


print(student["course"])

# Output:
# AI/ML



# =========================================================
# SET
# =========================================================

# Set stores unique values only.
# Duplicate values are automatically removed.

numbers = {1, 2, 3, 4, 4, 5, 5}

print(numbers)

# Output:
# {1, 2, 3, 4, 5}


# Notice:
# Duplicate values 4 and 5 are removed automatically.



# =========================================================
# 2. CUSTOMIZED DATA STRUCTURES
# =========================================================

# These data structures are created manually by programmers.

# Stack
# Queue
# Linked List
# Trees
# Graphs


# =========================================================
# STACK
# =========================================================

# Stack works on LIFO principle
# LIFO = Last In First Out

stack = []

# Adding elements
stack.append(10)
stack.append(20)
stack.append(30)

print(stack)

# Output:
# [10, 20, 30]


# Removing last element
stack.pop()

print(stack)

# Output:
# [10, 20]


# Example:
# Like a stack of plates.



# =========================================================
# QUEUE
# =========================================================

# Queue works on FIFO principle
# FIFO = First In First Out

queue = []

# Adding elements
queue.append("A")
queue.append("B")
queue.append("C")

print(queue)

# Output:
# ['A', 'B', 'C']


# Removing first element
queue.pop(0)

print(queue)

# Output:
# ['B', 'C']


# Example:
# Like people standing in line.



# =========================================================
# LINKED LIST
# =========================================================

# Linked List is a collection of connected nodes.

# Each node stores:
# 1. Data
# 2. Address of next node

# We will study this later in detail.



# =========================================================
# TREES
# =========================================================

# Tree is a hierarchical data structure.

# Example:
# Family Tree
# Folder Structure

# We will study this later in detail.



# =========================================================
# GRAPHS
# =========================================================

# Graph is a network of connected nodes.

# Example:
# Google Maps
# Social Media Connections

# We will study this later in detail.



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Data Structures store multiple values.
# 2. List is mutable (changeable).
# 3. Tuple is immutable (not changeable).
# 4. Dictionary stores key-value pairs.
# 5. Set stores unique values only.
# 6. Stack follows LIFO.
# 7. Queue follows FIFO.
# 8. Linked Lists, Trees, and Graphs are advanced structures.



# =========================================================
# IN THIS COURSE
# =========================================================

# In this course we will mainly focus on:
# - List
# - Tuple
# - Dictionary
# - Set

# These are Python In-built Data Structures.


# =========================================================
# END
# =========================================================







# =========================================================
# INTRODUCTION TO LIST IN PYTHON
# =========================================================


# =========================================================
# WHAT IS A LIST?
# =========================================================

# When we want to store multiple values
# inside one variable, we use List.

# Example:

students = ["Ruchit", "Rahul", "Aman"]

print(students)

# Output:
# ['Ruchit', 'Rahul', 'Aman']



# =========================================================
# SYNTAX OF LIST
# =========================================================

# List is created using square brackets [ ]

numbers = [10, 20, 30, 40]

print(numbers)

# Output:
# [10, 20, 30, 40]



# =========================================================
# INDEXING IN LIST
# =========================================================

# Indexing is similar to Strings.
# Index starts from 0.

names = ["Ruchit", "Rahul", "Aman", "Priya"]

print(names[0])
print(names[1])
print(names[2])

# Output:
# Ruchit
# Rahul
# Aman


# Negative Indexing

print(names[-1])

# Output:
# Priya



# =========================================================
# SLICING IN LIST
# =========================================================

# Slicing is also similar to Strings.

# Syntax:
# list[start : stop : step]

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[0:3])

# Output:
# [10, 20, 30]


print(numbers[1:5])

# Output:
# [20, 30, 40, 50]


print(numbers[0:6:2])

# Output:
# [10, 30, 50]


print(numbers[::-1])

# Output:
# [60, 50, 40, 30, 20, 10]



# =========================================================
# HETEROGENEOUS NATURE OF LIST
# =========================================================

# List can store different types of data together.

data = ["Ruchit", 20, 85.5, True]

print(data)

# Output:
# ['Ruchit', 20, 85.5, True]


# Different data structures inside list

mixed_data = [
    "Python",
    [1, 2, 3],
    (10, 20),
    {"name": "Ruchit"},
]

print(mixed_data)

# Output:
# ['Python', [1, 2, 3], (10, 20), {'name': 'Ruchit'}]



# =========================================================
# MUTABLE NATURE OF LIST
# =========================================================

# Mutable means values can be changed.

fruits = ["Apple", "Banana", "Mango"]

print(f"Before Change : {fruits}")

# Output:
# Before Change : ['Apple', 'Banana', 'Mango']


# Changing value
fruits[1] = "Orange"

print(f"After Change : {fruits}")

# Output:
# After Change : ['Apple', 'Orange', 'Mango']



# =========================================================
# SHALLOW COPY
# =========================================================

# In shallow copy, both variables point
# to same memory location.

list1 = [10, 20, 30]

list2 = list1

list2[0] = 100

print(list1)
print(list2)

# Output:
# [100, 20, 30]
# [100, 20, 30]


# Explanation:
# Changes in list2 also affect list1.



# =========================================================
# DEEP COPY
# =========================================================

# Deep copy creates a completely new copy.

import copy

list1 = [10, 20, 30]

list2 = copy.deepcopy(list1)

list2[0] = 100

print(list1)
print(list2)

# Output:
# [10, 20, 30]
# [100, 20, 30]


# Explanation:
# Changes in list2 do NOT affect list1.



# =========================================================
# LIST TRAVERSING
# =========================================================

# Traversing means accessing elements one by one.



# =========================================================
# TRAVERSING BASED ON VALUES
# =========================================================

names = ["Ruchit", "Rahul", "Aman"]

for value in names:
    print(value)

# Output:
# Ruchit
# Rahul
# Aman



# =========================================================
# TRAVERSING BASED ON INDEX
# =========================================================

names = ["Ruchit", "Rahul", "Aman"]

for index in range(len(names)):
    print(f"Index : {index} | Value : {names[index]}")

# Output:
# Index : 0 | Value : Ruchit
# Index : 1 | Value : Rahul
# Index : 2 | Value : Aman



# =========================================================
# LIST METHODS
# =========================================================



# =========================================================
# append()
# =========================================================

# append() adds value at end of list.

numbers = [10, 20, 30]

numbers.append(40)

print(numbers)

# Output:
# [10, 20, 30, 40]



# =========================================================
# pop()
# =========================================================

# pop() removes last value by default.

numbers = [10, 20, 30]

numbers.pop()

print(numbers)

# Output:
# [10, 20]


# Removing using index

numbers = [10, 20, 30, 40]

numbers.pop(1)

print(numbers)

# Output:
# [10, 30, 40]



# =========================================================
# reverse()
# =========================================================

# reverse() reverses the list.

numbers = [10, 20, 30, 40]

numbers.reverse()

print(numbers)

# Output:
# [40, 30, 20, 10]



# =========================================================
# GENERAL METHODS OF LIST
# =========================================================

# dir() shows all methods/functions available.

print(dir(list))

# Output:
# Large list of all list methods


# help() gives detailed explanation.

help(list)

# Output:
# Complete documentation of list methods



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. List stores multiple values.
# 2. List uses square brackets [ ].
# 3. Indexing and slicing are similar to Strings.
# 4. List is mutable (changeable).
# 5. List can store different data types together.
# 6. append() adds element.
# 7. pop() removes element.
# 8. reverse() reverses list.
# 9. Traversing means accessing values one by one.
# 10. Shallow copy shares same memory.
# 11. Deep copy creates separate memory.



# =========================================================
# END OF LIST INTRODUCTION
# =========================================================




# =========================================================
# INTRODUCTION TO TUPLE IN PYTHON
# =========================================================


# =========================================================
# WHAT IS A TUPLE?
# =========================================================

# Tuple is also used to store multiple values.

students = ("Ruchit", "Rahul", "Aman")

print(students)

# Output:
# ('Ruchit', 'Rahul', 'Aman')



# =========================================================
# SYNTAX OF TUPLE
# =========================================================

# Tuple is created using parenthesis ()

numbers = (10, 20, 30, 40)

print(numbers)

# Output:
# (10, 20, 30, 40)



# =========================================================
# INDEXING IN TUPLE
# =========================================================

# Indexing is similar to List.
# Index starts from 0.

names = ("Ruchit", "Rahul", "Aman", "Priya")

print(names[0])
print(names[1])
print(names[2])

# Output:
# Ruchit
# Rahul
# Aman


# Negative Indexing

print(names[-1])

# Output:
# Priya



# =========================================================
# TUPLE SLICING
# =========================================================

# Slicing is also similar to List.

# Syntax:
# tuple[start : stop : step]

numbers = (10, 20, 30, 40, 50, 60)

print(numbers[0:3])

# Output:
# (10, 20, 30)


print(numbers[1:5])

# Output:
# (20, 30, 40, 50)


print(numbers[0:6:2])

# Output:
# (10, 30, 50)


print(numbers[::-1])

# Output:
# (60, 50, 40, 30, 20, 10)



# =========================================================
# SINGLE ELEMENT TUPLE
# =========================================================

# To create single element tuple,
# comma is compulsory.

a = (10)

print(type(a))

# Output:
# <class 'int'>


# Correct way

b = (10,)

print(type(b))

# Output:
# <class 'tuple'>



# =========================================================
# IMMUTABLE NATURE OF TUPLE
# =========================================================

# Tuple values cannot be changed.

colors = ("Red", "Green", "Blue")

print(colors)

# Output:
# ('Red', 'Green', 'Blue')


# colors[1] = "Yellow"
# Error because tuple is immutable.



# =========================================================
# tuple() CONSTRUCTOR
# =========================================================

# tuple() converts iterable into tuple.

my_list = [10, 20, 30]

converted_tuple = tuple(my_list)

print(converted_tuple)

# Output:
# (10, 20, 30)



# =========================================================
# TUPLE UNPACKING
# =========================================================

# Storing tuple values into separate variables.

student = ("Ruchit", 20, "AI/ML")

name, age, course = student

print(name)
print(age)
print(course)

# Output:
# Ruchit
# 20
# AI/ML



# =========================================================
# TUPLE TRAVERSING
# =========================================================

# Traversing means accessing values one by one.



# =========================================================
# TRAVERSING BASED ON VALUES
# =========================================================

names = ("Ruchit", "Rahul", "Aman")

for value in names:
    print(value)

# Output:
# Ruchit
# Rahul
# Aman



# =========================================================
# TRAVERSING BASED ON INDEX
# =========================================================

names = ("Ruchit", "Rahul", "Aman")

for index in range(len(names)):
    print(f"Index : {index} | Value : {names[index]}")

# Output:
# Index : 0 | Value : Ruchit
# Index : 1 | Value : Rahul
# Index : 2 | Value : Aman



# =========================================================
# TUPLE METHODS
# =========================================================

# Tuple has very few methods because it is immutable.



# =========================================================
# count()
# =========================================================

# count() counts occurrence of value.

numbers = (10, 20, 10, 30, 10)

print(numbers.count(10))

# Output:
# 3



# =========================================================
# index()
# =========================================================

# index() returns position of value.

numbers = (10, 20, 30, 40)

print(numbers.index(30))

# Output:
# 2



# =========================================================
# GENERAL TUPLE METHODS
# =========================================================

# dir() shows all available methods.

print(dir(tuple))

# Output:
# Large list of tuple methods


# help() gives detailed explanation.

help(tuple)

# Output:
# Complete documentation of tuple



# =========================================================
# DIFFERENCE BETWEEN LIST AND TUPLE
# =========================================================

# LIST
# - Uses square brackets []
# - Mutable
# - More methods

# TUPLE
# - Uses parenthesis ()
# - Immutable
# - Fewer methods



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Tuple stores multiple values.
# 2. Tuple uses parenthesis ().
# 3. Indexing and slicing are similar to List.
# 4. Tuple is immutable.
# 5. Single element tuple requires comma.
# 6. tuple() converts list into tuple.
# 7. Tuple unpacking separates values into variables.
# 8. count() and index() are common tuple methods.
# 9. Traversing means accessing values one by one.



# =========================================================
# END OF TUPLE INTRODUCTION
# =========================================================





# =========================================================
# INTRODUCTION TO SET IN PYTHON
# =========================================================


# =========================================================
# WHAT IS A SET?
# =========================================================

# Set is also used to store multiple values.

numbers = {10, 20, 30, 40}

print(numbers)

# Output:
# {10, 20, 30, 40}



# =========================================================
# SYNTAX OF SET
# =========================================================

# Set is created using curly brackets { }

fruits = {"Apple", "Banana", "Mango"}

print(fruits)

# Output:
# {'Apple', 'Banana', 'Mango'}


# NOTE:
# Sets use curly brackets {} not ()
# Parenthesis () are used for Tuple.



# =========================================================
# UNORDERED NATURE OF SET
# =========================================================

# Set is unordered.
# That means:
# - No fixed position
# - No indexing
# - No slicing

numbers = {10, 20, 30, 40}

print(numbers)

# Output can be:
# {40, 10, 20, 30}

# OR
# {10, 20, 30, 40}

# Order may change every time.



# =========================================================
# NO INDEXING IN SET
# =========================================================

# Set does not support indexing.

numbers = {10, 20, 30}

# print(numbers[0])

# Output:
# TypeError: 'set' object is not subscriptable



# =========================================================
# MUTABLE NATURE OF SET
# =========================================================

# Even though Set is unordered,
# it is still mutable.

# Mutable means values can be added or removed.

numbers = {10, 20, 30}

print(f"Before : {numbers}")

# Output:
# Before : {10, 20, 30}


# Adding value
numbers.add(40)

print(f"After Adding : {numbers}")

# Output:
# After Adding : {10, 20, 30, 40}


# Removing value
numbers.remove(20)

print(f"After Removing : {numbers}")

# Output:
# After Removing : {10, 30, 40}



# =========================================================
# NO DUPLICATE VALUES
# =========================================================

# Set automatically removes duplicate values.

numbers = {10, 20, 30, 10, 20, 40}

print(numbers)

# Output:
# {10, 20, 30, 40}



# =========================================================
# set() CONSTRUCTOR
# =========================================================

# set() converts iterable into set.

my_list = [10, 20, 30, 10, 20]

converted_set = set(my_list)

print(converted_set)

# Output:
# {10, 20, 30}


# Duplicate values removed automatically.



# =========================================================
# SET TRAVERSING
# =========================================================

# Traversing means accessing values one by one.



# =========================================================
# TRAVERSING BASED ON VALUES
# =========================================================

# Traversing in Set happens on the basis
# of hash values internally.

names = {"Ruchit", "Rahul", "Aman"}

for value in names:
    print(value)

# Output can be:
# Rahul
# Aman
# Ruchit

# Order is not fixed.



# =========================================================
# NO TRAVERSING BASED ON INDEX
# =========================================================

# Since Set has no indexing,
# traversing using range() is not possible.

numbers = {10, 20, 30}

# for i in range(len(numbers)):
#     print(numbers[i])

# Output:
# TypeError



# =========================================================
# SET METHODS
# =========================================================

# Set heavily depends on methods.



# =========================================================
# add()
# =========================================================

# add() adds one value.

numbers = {10, 20, 30}

numbers.add(40)

print(numbers)

# Output:
# {10, 20, 30, 40}



# =========================================================
# update()
# =========================================================

# update() adds multiple values.

numbers = {10, 20}

numbers.update([30, 40, 50])

print(numbers)

# Output:
# {10, 20, 30, 40, 50}



# =========================================================
# remove()
# =========================================================

# remove() removes value.

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)

# Output:
# {10, 30}



# =========================================================
# discard()
# =========================================================

# discard() removes value safely.

numbers = {10, 20, 30}

numbers.discard(50)

print(numbers)

# Output:
# {10, 20, 30}

# No error if value does not exist.



# =========================================================
# pop()
# =========================================================

# pop() removes random value.

numbers = {10, 20, 30}

numbers.pop()

print(numbers)

# Output can be:
# {20, 30}

# Random element removed.



# =========================================================
# clear()
# =========================================================

# clear() removes all values.

numbers = {10, 20, 30}

numbers.clear()

print(numbers)

# Output:
# set()



# =========================================================
# VENN DIAGRAM APPROACH
# =========================================================

# Sets are highly used in mathematics.

# Example:
# Union
# Intersection
# Difference



# =========================================================
# UNION
# =========================================================

# Combines all unique values.

a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))

# Output:
# {1, 2, 3, 4, 5}



# =========================================================
# INTERSECTION
# =========================================================

# Common values between sets.

a = {1, 2, 3}
b = {2, 3, 4}

print(a.intersection(b))

# Output:
# {2, 3}



# =========================================================
# DIFFERENCE
# =========================================================

# Values present in first set only.

a = {1, 2, 3}
b = {2, 3, 4}

print(a.difference(b))

# Output:
# {1}



# =========================================================
# GENERAL METHODS
# =========================================================

# dir() shows all available methods.

print(dir(set))

# Output:
# Large list of set methods


# help() gives complete documentation.

help(set)

# Output:
# Complete explanation of set methods



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Set stores multiple values.
# 2. Set uses curly brackets {}.
# 3. Set is unordered.
# 4. Set has no indexing and no slicing.
# 5. Set does not allow duplicate values.
# 6. Set is mutable.
# 7. add() adds single value.
# 8. update() adds multiple values.
# 9. remove() removes value.
# 10. Sets are heavily method-based.
# 11. Union, Intersection, Difference are important operations.



# =========================================================
# END OF SET INTRODUCTION
# =========================================================





# =========================================================
# INTRODUCTION TO DICTIONARY IN PYTHON
# =========================================================


# =========================================================
# WHAT IS A DICTIONARY?
# =========================================================

# Dictionary is also used to store multiple values.
# Unlike Set, Dictionary stores data in key-value pairs.

student = {
    "name": "Ruchit",
    "age": 20,
    "course": "AI/ML"
}

print(student)

# Output:
# {'name': 'Ruchit', 'age': 20, 'course': 'AI/ML'}



# =========================================================
# SYNTAX OF DICTIONARY
# =========================================================

# Dictionary uses curly brackets {}
# with key : value format.

car = {
    "brand": "BMW",
    "model": "M5",
    "year": 2025
}

print(car)

# Output:
# {'brand': 'BMW', 'model': 'M5', 'year': 2025}



# =========================================================
# ACCESSING VALUES
# =========================================================

# Values are accessed using keys.

student = {
    "name": "Ruchit",
    "age": 20
}

print(student["name"])

# Output:
# Ruchit


print(student["age"])

# Output:
# 20



# =========================================================
# ORDERED NATURE OF DICTIONARY
# =========================================================

# Before Python 3.7:
# Dictionary was unordered.

# Modern Python:
# Dictionary maintains insertion order.

data = {
    "a": 10,
    "b": 20,
    "c": 30
}

print(data)

# Output:
# {'a': 10, 'b': 20, 'c': 30}



# =========================================================
# MUTABLE NATURE OF DICTIONARY
# =========================================================

# Dictionary is mutable.
# We can change values.

student = {
    "name": "Ruchit",
    "age": 20
}

print(f"Before Change : {student}")

# Output:
# Before Change : {'name': 'Ruchit', 'age': 20}


# Changing value
student["age"] = 21

print(f"After Change : {student}")

# Output:
# After Change : {'name': 'Ruchit', 'age': 21}



# =========================================================
# ADDING NEW ITEMS
# =========================================================

student = {
    "name": "Ruchit"
}

student["course"] = "AI/ML"

print(student)

# Output:
# {'name': 'Ruchit', 'course': 'AI/ML'}



# =========================================================
# REMOVING ITEMS
# =========================================================

student = {
    "name": "Ruchit",
    "age": 20
}

del student["age"]

print(student)

# Output:
# {'name': 'Ruchit'}



# =========================================================
# NO DUPLICATE KEYS
# =========================================================

# Duplicate keys are not allowed.
# Latest value overwrites old value.

data = {
    "name": "Ruchit",
    "name": "Rahul"
}

print(data)

# Output:
# {'name': 'Rahul'}



# =========================================================
# DUPLICATE VALUES ALLOWED
# =========================================================

data = {
    "student1": "Ruchit",
    "student2": "Ruchit"
}

print(data)

# Output:
# {'student1': 'Ruchit', 'student2': 'Ruchit'}



# =========================================================
# dict() CONSTRUCTOR
# =========================================================

# dict() can also create dictionary.

student = dict(
    name="Ruchit",
    age=20,
    course="AI/ML"
)

print(student)

# Output:
# {'name': 'Ruchit', 'age': 20, 'course': 'AI/ML'}



# =========================================================
# DICTIONARY TRAVERSING
# =========================================================

# Traversing means accessing items one by one.



# =========================================================
# TRAVERSING BASED ON KEYS
# =========================================================

student = {
    "name": "Ruchit",
    "age": 20,
    "course": "AI/ML"
}

for key in student:
    print(key)

# Output:
# name
# age
# course



# =========================================================
# ACCESSING VALUES USING KEYS
# =========================================================

student = {
    "name": "Ruchit",
    "age": 20,
    "course": "AI/ML"
}

for key in student:
    print(f"{key} : {student[key]}")

# Output:
# name : Ruchit
# age : 20
# course : AI/ML



# =========================================================
# TRAVERSING VALUES ONLY
# =========================================================

student = {
    "name": "Ruchit",
    "age": 20,
    "course": "AI/ML"
}

for value in student.values():
    print(value)

# Output:
# Ruchit
# 20
# AI/ML



# =========================================================
# TRAVERSING KEY-VALUE PAIRS
# =========================================================

student = {
    "name": "Ruchit",
    "age": 20,
    "course": "AI/ML"
}

for key, value in student.items():
    print(f"{key} : {value}")

# Output:
# name : Ruchit
# age : 20
# course : AI/ML



# =========================================================
# DICTIONARY METHODS
# =========================================================

# Dictionary has useful methods.



# =========================================================
# keys()
# =========================================================

# keys() returns all keys.

student = {
    "name": "Ruchit",
    "age": 20
}

print(student.keys())

# Output:
# dict_keys(['name', 'age'])



# =========================================================
# values()
# =========================================================

# values() returns all values.

student = {
    "name": "Ruchit",
    "age": 20
}

print(student.values())

# Output:
# dict_values(['Ruchit', 20])



# =========================================================
# items()
# =========================================================

# items() returns key-value pairs.

student = {
    "name": "Ruchit",
    "age": 20
}

print(student.items())

# Output:
# dict_items([('name', 'Ruchit'), ('age', 20)])



# =========================================================
# get()
# =========================================================

# get() safely accesses value.

student = {
    "name": "Ruchit"
}

print(student.get("name"))

# Output:
# Ruchit


print(student.get("age"))

# Output:
# None



# =========================================================
# pop()
# =========================================================

# pop() removes item using key.

student = {
    "name": "Ruchit",
    "age": 20
}

student.pop("age")

print(student)

# Output:
# {'name': 'Ruchit'}



# =========================================================
# update()
# =========================================================

# update() adds or updates items.

student = {
    "name": "Ruchit"
}

student.update({"age": 20})

print(student)

# Output:
# {'name': 'Ruchit', 'age': 20}



# =========================================================
# clear()
# =========================================================

# clear() removes all items.

student = {
    "name": "Ruchit",
    "age": 20
}

student.clear()

print(student)

# Output:
# {}



# =========================================================
# GENERAL METHODS
# =========================================================

# dir() shows all available methods.

print(dir(dict))

# Output:
# Large list of dictionary methods


# help() gives complete documentation.

help(dict)

# Output:
# Complete explanation of dictionary methods



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Dictionary stores data in key-value pairs.
# 2. Dictionary uses curly brackets {}.
# 3. Keys must be unique.
# 4. Values can be duplicated.
# 5. Dictionary is mutable.
# 6. Modern dictionaries maintain insertion order.
# 7. Traversing can be done using keys and values.
# 8. keys(), values(), items() are important methods.
# 9. get() safely accesses values.
# 10. update() adds or updates items.



# =========================================================
# END OF DICTIONARY INTRODUCTION
# =========================================================




# =========================================================
# ADVANCED PYTHON CONCEPTS
# =========================================================

# In this section we will learn:
# 1. Lambda Expression
# 2. Map
# 3. Filter
# 4. Zip
# 5. List Comprehension
# 6. Dictionary Comprehension
# 7. Set Comprehension
# 8. Generators
# 9. Decorators



# =========================================================
# LAMBDA EXPRESSION
# =========================================================

# Lambda is a small anonymous function.

# Syntax:
# lambda arguments : expression


# Normal Function

def square(num):
    return num * num

print(square(5))

# Output:
# 25


# Lambda Function

square = lambda num: num * num

print(square(5))

# Output:
# 25



# =========================================================
# MAP FUNCTION
# =========================================================

# map() applies function on every element.

numbers = [1, 2, 3, 4, 5]

square = list(map(lambda x: x * x, numbers))

print(square)

# Output:
# [1, 4, 9, 16, 25]



# =========================================================
# FILTER FUNCTION
# =========================================================

# filter() filters values based on condition.

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

# Output:
# [2, 4, 6]



# =========================================================
# ZIP FUNCTION
# =========================================================

# zip() combines multiple iterables together.

names = ["Ruchit", "Rahul", "Aman"]
marks = [90, 80, 70]

combined = list(zip(names, marks))

print(combined)

# Output:
# [('Ruchit', 90), ('Rahul', 80), ('Aman', 70)]



# =========================================================
# LIST COMPREHENSION
# =========================================================

# Short trick for creating lists.

# Traditional Method

numbers = []

for i in range(1, 6):
    numbers.append(i)

print(numbers)

# Output:
# [1, 2, 3, 4, 5]


# List Comprehension

numbers = [i for i in range(1, 6)]

print(numbers)

# Output:
# [1, 2, 3, 4, 5]



# =========================================================
# LIST COMPREHENSION WITH CONDITION
# =========================================================

even_numbers = [i for i in range(1, 11) if i % 2 == 0]

print(even_numbers)

# Output:
# [2, 4, 6, 8, 10]



# =========================================================
# DICTIONARY COMPREHENSION
# =========================================================

# Creating dictionary in short way.

numbers = {i: i * i for i in range(1, 6)}

print(numbers)

# Output:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}



# =========================================================
# SET COMPREHENSION
# =========================================================

# Creating set in short way.

numbers = {i * 2 for i in range(1, 6)}

print(numbers)

# Output:
# {2, 4, 6, 8, 10}



# =========================================================
# GENERATORS
# =========================================================

# Generators are used to generate values one by one.

# Advantage:
# Memory efficient



# =========================================================
# GENERATOR FUNCTION
# =========================================================

# yield keyword makes function generator.

def numbers():

    yield 1
    yield 2
    yield 3


data = numbers()

print(next(data))
print(next(data))
print(next(data))

# Output:
# 1
# 2
# 3



# =========================================================
# GENERATOR USING LOOP
# =========================================================

def count():

    for i in range(1, 6):
        yield i


data = count()

for value in data:
    print(value)

# Output:
# 1
# 2
# 3
# 4
# 5



# =========================================================
# GENERATOR EXPRESSION
# =========================================================

# Similar to list comprehension
# but uses parenthesis ()

numbers = (i * i for i in range(1, 6))

print(numbers)

# Output:
# <generator object ...>


for value in numbers:
    print(value)

# Output:
# 1
# 4
# 9
# 16
# 25



# =========================================================
# GENERATOR COMPREHENSION
# =========================================================

# Generator expressions are also called
# generator comprehension.

even_numbers = (i for i in range(1, 11) if i % 2 == 0)

for value in even_numbers:
    print(value)

# Output:
# 2
# 4
# 6
# 8
# 10



# =========================================================
# DECORATORS
# =========================================================

# Decorators are used to modify behavior
# of another function.



# =========================================================
# WHAT IS DECORATOR?
# =========================================================

# Decorator is a function
# that takes another function as argument.



# =========================================================
# CREATING DECORATOR
# =========================================================

def decorator_function(original_function):

    def wrapper_function():

        print("Before Function Execution")

        original_function()

        print("After Function Execution")

    return wrapper_function



# Original Function

def display():
    print("Hello Ruchit")


# Applying Decorator

decorated_function = decorator_function(display)

decorated_function()

# Output:
# Before Function Execution
# Hello Ruchit
# After Function Execution



# =========================================================
# USING @ DECORATOR SYMBOL
# =========================================================

# Cleaner way to use decorators.

def decorator_function(original_function):

    def wrapper_function():

        print("Decorator Started")

        original_function()

        print("Decorator Ended")

    return wrapper_function


@decorator_function
def greet():
    print("Welcome to Python")


greet()

# Output:
# Decorator Started
# Welcome to Python
# Decorator Ended



# =========================================================
# IMPORTANT POINTS
# =========================================================

# 1. Lambda is anonymous function.
# 2. map() transforms data.
# 3. filter() filters data.
# 4. zip() combines iterables.
# 5. Comprehensions provide short syntax.
# 6. Generators save memory.
# 7. yield creates generator.
# 8. Decorators modify function behavior.
# 9. @ symbol is shortcut for decorators.



# =========================================================
# END OF ADVANCED PYTHON
# =========================================================