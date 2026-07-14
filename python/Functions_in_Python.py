# ==========================================================
#                    FUNCTIONS IN PYTHON
# ==========================================================
#
# Description:
# A function is a reusable block of code that performs a
# specific task. Functions help reduce code repetition and
# make programs easier to read and maintain.
#
# Syntax:
# def function_name():
#     code
#
# function_name()   # Calling the function
#
# ==========================================================


# =======================
# 1. SIMPLE FUNCTION
# =======================
print("----- SIMPLE FUNCTION -----")

def greet():
    print("Hello, Welcome to Python!")

greet()

# Output:
# Hello, Welcome to Python!


# =======================
# 2. PRINT VS RETURN
# =======================
print("\n----- PRINT VS RETURN -----")

# Function using print
def using_print():
    print("This is printed inside the function")

using_print()

# Function using return
def using_return():
    return "This value is returned"

result = using_return()
print(result)

# Output:
# This is printed inside the function
# This value is returned


# =======================
# 3. IMPERATIVE VS FUNCTIONAL CODE
# =======================
print("\n----- IMPERATIVE VS FUNCTIONAL CODE -----")

# Imperative Code
print("Hello")
print("Hello")
print("Hello")

# Functional Code
def hello():
    print("Hello")

hello()
hello()
hello()

# Output:
# Hello
# Hello
# Hello
# Hello
# Hello
# Hello


# =======================
# 4. PARAMETERS AND ARGUMENTS
# =======================
print("\n----- PARAMETERS AND ARGUMENTS -----")

def student(name):
    print("Student Name:", name)

student("Ruchit")

# Parameter  -> name
# Argument   -> "Ruchit"

# Output:
# Student Name: Ruchit


# =======================
# 5. MULTIPLE PARAMETERS
# =======================
print("\n----- MULTIPLE PARAMETERS -----")

def add(a, b):
    print("Sum =", a + b)

add(10, 20)

# Parameters -> a, b
# Arguments  -> 10, 20

# Output:
# Sum = 30


# =======================
# 6. RETURN VALUE
# =======================
print("\n----- RETURN VALUE -----")

def multiply(a, b):
    return a * b

answer = multiply(5, 4)

print("Multiplication =", answer)

# Output:
# Multiplication = 20


# =======================
# 7. DEFAULT PARAMETERS
# =======================
print("\n----- DEFAULT PARAMETERS -----")

def country(name="India"):
    print("Country:", name)

country()
country("Canada")

# Output:
# Country: India
# Country: Canada


# =======================
# 8. KEYWORD ARGUMENTS
# =======================
print("\n----- KEYWORD ARGUMENTS -----")

def details(name, age):
    print("Name :", name)
    print("Age  :", age)

details(age=19, name="Ruchit")

# Output:
# Name : Ruchit
# Age  : 19


# =======================
# 9. DEFAULT PARAMETERS WITH VALUES
# =======================
print("\n----- PARAMETERS WITH DEFAULT VALUES -----")

def employee(name, city="Ahmedabad"):
    print(name, "-", city)

employee("Ruchit")
employee("Rahul", "Surat")

# Output:
# Ruchit - Ahmedabad
# Rahul - Surat


# =======================
# 10. INTRODUCTION TO *args
# =======================
print("\n----- *args (Introduction) -----")

def numbers(*args):
    print(args)

numbers(10, 20, 30, 40)

# Output:
# (10, 20, 30, 40)

# *args allows multiple positional arguments.
# (Detailed study later.)


# =======================
# 11. INTRODUCTION TO **kwargs
# =======================
print("\n----- **kwargs (Introduction) -----")

def information(**kwargs):
    print(kwargs)

information(name="Ruchit", age=19)

# Output:
# {'name': 'Ruchit', 'age': 19}

# **kwargs allows multiple keyword arguments.
# (Detailed study later.)


# ==========================================================
# IMPORTANT NOTES
# ==========================================================
#
# print()
# - Displays the output on the terminal.
#
# return
# - Sends the result back to the place where the function
#   was called.
#
# Parameter
# - Variable written in the function definition.
#
# Argument
# - Actual value passed while calling the function.
#
# ==========================================================


# ==========================================================
# COMMIT:
# Learned Python Functions including function creation using
# def, function calling, print vs return, parameters,
# arguments, keyword arguments, default parameters,
# introduction to *args and **kwargs, and the difference
# between imperative and functional programming.
# ==========================================================