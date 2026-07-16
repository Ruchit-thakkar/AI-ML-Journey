# ==========================================================
# PYTHON NOTES - Lambda, Map, Filter, Zip & Comprehensions
# ==========================================================

# ----------------------------------------------------------
# 1. Lambda Function
# ----------------------------------------------------------
# A lambda function is a small anonymous (nameless) function.
# Syntax:
# lambda arguments : expression
#
# It can have any number of arguments but only one expression.
# The expression is automatically returned.

# Example: Square of a number

square = lambda a: a ** 2

print(square(12))

# Output:
# 144
#
# Explanation:
# a = 12
# 12 ** 2 = 144


print("--------------------------------")


# Example: Add two numbers

add = lambda x, y: x + y

print(add(12, 13))

# Output:
# 25
#
# Explanation:
# x = 12
# y = 13
# 12 + 13 = 25


print("--------------------------------")


# ----------------------------------------------------------
# 2. map()
# ----------------------------------------------------------
# map() applies a function to every element in an iterable.
#
# Syntax:
# map(function, iterable)

a = [1, 2, 3, 4, 5]

l = map(lambda x: x ** 2, a)

print(list(l))

# Output:
# [1, 4, 9, 16, 25]
#
# How it works:
# 1 -> 1² = 1
# 2 -> 2² = 4
# 3 -> 3² = 9
# 4 -> 4² = 16
# 5 -> 5² = 25
#
# map() returns a map object.
# We convert it into a list using list().


print("--------------------------------")


# ----------------------------------------------------------
# 3. filter()
# ----------------------------------------------------------
# filter() selects elements that satisfy a condition.
#
# Syntax:
# filter(function, iterable)

a = [1, 2, 3, 4, 5]

l = filter(lambda x: x % 2 == 0, a)

print(list(l))

# Output:
# [2, 4]
#
# How it works:
# 1 % 2 = 1 ❌
# 2 % 2 = 0 ✅
# 3 % 2 = 1 ❌
# 4 % 2 = 0 ✅
# 5 % 2 = 1 ❌
#
# Only even numbers are returned.


print("--------------------------------")


# ----------------------------------------------------------
# 4. zip()
# ----------------------------------------------------------
# zip() combines multiple iterables element by element.
#
# Syntax:
# zip(iterable1, iterable2)

name = ["ruchit", "ashok", "hema"]
age = [20, 66, 61]

combine = zip(name, age)

print(dict(list(combine)))

# Output:
# {'ruchit': 20, 'ashok': 66, 'hema': 61}
#
# How it works:
#
# "ruchit" -> 20
# "ashok"  -> 66
# "hema"   -> 61
#
# zip() creates pairs:
#
# ('ruchit',20)
# ('ashok',66)
# ('hema',61)
#
# Then dict() converts those pairs into a dictionary.


print("--------------------------------")


# ----------------------------------------------------------
# 5. List Comprehension
# ----------------------------------------------------------
# Creates a list in a single line.
#
# Syntax:
# [expression for item in iterable if condition]

a = [1,2,3,4,5,6,7,8,9]

l = [i for i in a if i % 2 == 0]

print(l)

# Output:
# [2, 4, 6, 8]
#
# How it works:
#
# Loop through every number.
# Keep only even numbers.
#
# Equivalent to:
#
# result = []
# for i in a:
#     if i % 2 == 0:
#         result.append(i)


print("--------------------------------")


# ----------------------------------------------------------
# 6. Set Comprehension
# ----------------------------------------------------------
# Creates a set in one line.
#
# Syntax:
# {expression for item in iterable if condition}

a = [1,2,3,4,5,6,7,8,9]

l = {i for i in a if i % 2 == 0}

print(l)

# Output:
# {2, 4, 6, 8}
#
# Explanation:
# Same as list comprehension,
# but stores data inside a SET.
#
# A set:
# ✔ Stores unique values
# ✔ Does not maintain duplicates


print("--------------------------------")


# ----------------------------------------------------------
# 7. Dictionary Comprehension
# ----------------------------------------------------------
# Creates a dictionary in one line.
#
# Syntax:
# {key:value for item in iterable if condition}

a = [1,2,3,4,5,6,7,8,9]

l = {i: i ** 2 for i in a if i % 2 == 0}

print(l)

# Output:
# {2: 4, 4: 16, 6: 36, 8: 64}
#
# How it works:
#
# Key : Value
# 2   : 4
# 4   : 16
# 6   : 36
# 8   : 64
#
# Equivalent to:
#
# result = {}
# for i in a:
#     if i % 2 == 0:
#         result[i] = i ** 2


print("--------------------------------")


# ==========================================================
# SUMMARY
# ==========================================================
#
# lambda
# -------
# Small anonymous function.
#
# map()
# -----
# Applies a function to every element.
#
# filter()
# --------
# Returns elements that satisfy a condition.
#
# zip()
# -----
# Combines multiple iterables element-wise.
#
# List Comprehension
# ------------------
# Creates a list in one line.
#
# Set Comprehension
# -----------------
# Creates a set in one line.
#
# Dictionary Comprehension
# ------------------------
# Creates a dictionary in one line.
#
# ==========================================================
# ==========================================================
# PYTHON NOTES - Generators & Decorators
# ==========================================================

# ----------------------------------------------------------
# 1. Generator Function
# ----------------------------------------------------------
# A generator is a special function that returns values
# one at a time using the 'yield' keyword.
#
# Unlike 'return', 'yield' pauses the function and remembers
# its current state. The next time next() is called,
# execution continues from where it stopped.

def my_gen():
    for i in range(5):
        yield i

gen = my_gen()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

# Output:
# 0
# 1
# 2
# 3
# 4
#
# How it works:
#
# First next()  -> yield 0
# Second next() -> yield 1
# Third next()  -> yield 2
# Fourth next() -> yield 3
# Fifth next()  -> yield 4
#
# After this,
# next(gen)
# will raise:
#
# StopIteration
#
# because there are no more values.


print("--------------------------------")


# ----------------------------------------------------------
# 2. Generator Expression
# ----------------------------------------------------------
# A generator expression is a shorter way to create
# a generator.
#
# Syntax:
# (expression for item in iterable)

square = (x ** 2 for x in range(5))

print(next(square))
print(next(square))
print(next(square))
print(next(square))

# Output:
# 0
# 1
# 4
# 9
#
# Explanation:
#
# range(5)
# 0 -> 0² = 0
# 1 -> 1² = 1
# 2 -> 2² = 4
# 3 -> 3² = 9
# 4 -> 4² = 16
#
# Only the first four values are printed.
#
# If we call:
#
# print(next(square))
#
# Output:
# 16
#
# Another next(square)
# raises StopIteration.


print("--------------------------------")


# ==========================================================
# DECORATORS
# ==========================================================

# ----------------------------------------------------------
# What is a Decorator?
# ----------------------------------------------------------
#
# A decorator is a function that adds extra functionality
# to another function without changing its original code.
#
# Syntax:
#
# @decorator_name
# def function():
#     ...
#
# It is equivalent to:
#
# function = decorator_name(function)


# ----------------------------------------------------------
# 3. Simple Decorator
# ----------------------------------------------------------

def my_decorator(fun):

    # Wrapper function
    def wrapper():
        print("Print Before")

        # Call original function
        fun()

        print("Print After")

    return wrapper


@my_decorator
def say_hello():
    print("Hello World")


say_hello()

# Output:
#
# Print Before
# Hello World
# Print After
#
# How it works:
#
# Step 1:
# say_hello() is passed to my_decorator()
#
# Step 2:
# my_decorator() returns wrapper()
#
# Step 3:
# Calling say_hello() actually calls wrapper()
#
# wrapper():
#    Print Before
#    Original Function
#    Print After


print("--------------------------------")


# ----------------------------------------------------------
# 4. Decorator with Arguments
# ----------------------------------------------------------

def sum_decorator(fun):

    # Wrapper accepts parameters
    def wrapper(a, b):

        print("Sum of Two Numbers")

        # Call original function
        fun(a, b)

        print("Thank You For Using")

    return wrapper


@sum_decorator
def add(a, b):
    print(a + b)


add(12, 13)

# Output:
#
# Sum of Two Numbers
# 25
# Thank You For Using
#
# How it works:
#
# add(12,13)
#
# becomes
#
# wrapper(12,13)
#
# wrapper():
#
# Print message
# ↓
# Calls original add(12,13)
# ↓
# Prints 25
# ↓
# Prints Thank You message


print("--------------------------------")


# ==========================================================
# Difference: return vs yield
# ==========================================================
#
# return
# -------
# • Ends the function immediately.
# • Returns only one value.
# • Function does not remember its state.
#
# Example:
#
# def test():
#     return 10
#
#
# yield
# -----
# • Pauses the function.
# • Returns one value at a time.
# • Remembers where it stopped.
#
# Example:
#
# def test():
#     yield 10
#     yield 20
#
#
# ==========================================================
# Summary
# ==========================================================
#
# Generator
# ---------
# Uses 'yield' to generate values one by one.
#
# Generator Expression
# --------------------
# Short way to create generators.
#
# Decorator
# ---------
# Adds extra functionality to a function.
#
# Wrapper Function
# ----------------
# Executes code before and after the original function.
#
# @decorator
# ----------
# Shortcut for:
#
# function = decorator(function)
#
# ==========================================================