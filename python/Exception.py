# ==========================================================
# PYTHON NOTES - Exception Handling
# ==========================================================

# ----------------------------------------------------------
# What is an Exception?
# ----------------------------------------------------------
# An Exception is an error that occurs while a program
# is running (runtime error).
#
# If we do not handle exceptions, the program will stop
# immediately.
#
# Python provides exception handling using:
#
# try
# except
# else
# finally
#
# so that the program can continue running.


# ==========================================================
# 1. try - except - else - finally
# ==========================================================

# Taking input from the user
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    # Code that may generate an error
    print(a / b)

except Exception as err:
    # Runs only if an exception occurs
    print(f"This is error: {err}")

else:
    # Runs only if NO exception occurs
    print("There was no error.")

finally:
    # Runs every time
    # Whether an exception occurs or not
    print("I will execute no matter what!!")


# ----------------------------------------------------------
# Example Outputs
# ----------------------------------------------------------

# Example 1
#
# Input:
# Enter first number: 20
# Enter second number: 5
#
# Output:
# 4.0
# There was no error.
# I will execute no matter what!!
#
#
# Explanation:
# No error occurred.
#
# try     -> executed
# except  -> skipped
# else    -> executed
# finally -> executed


# ----------------------------------------------------------

# Example 2
#
# Input:
# Enter first number: 20
# Enter second number: 0
#
# Output:
#
# This is error: division by zero
# I will execute no matter what!!
#
#
# Explanation:
#
# Division by zero causes an exception.
#
# try     -> error occurred
# except  -> executed
# else    -> skipped
# finally -> executed


print("--------------------------------")


# ==========================================================
# 2. raise Exception
# ==========================================================
#
# Sometimes we want to create our own exception.
#
# Python provides:
#
# raise
#
# Syntax:
#
# raise Exception("Message")
#
# It immediately stops the current block
# and raises an exception.

try:
    age = int(input("Enter your age: "))

    if age <= 18:
        raise Exception("You must be 18+")

    else:
        print("You are 18+")

except Exception as err:
    print(err)


# ----------------------------------------------------------
# Example Outputs
# ----------------------------------------------------------

# Example 1
#
# Input:
# Enter your age: 16
#
# Output:
# You must be 18+
#
#
# Explanation:
#
# age <= 18
#
# raise Exception(...)
#
# jumps directly to except.


# ----------------------------------------------------------

# Example 2
#
# Input:
# Enter your age: 22
#
# Output:
# You are 18+
#
#
# Explanation:
#
# Condition is False.
#
# raise is NOT executed.
#
# except block is skipped.


print("--------------------------------")


# ==========================================================
# Flow of try-except-else-finally
# ==========================================================

# Case 1 (No Error)
#
# try
#   ↓
# else
#   ↓
# finally


# Case 2 (Error Occurs)
#
# try
#   ↓
# except
#   ↓
# finally


# ==========================================================
# Common Built-in Exceptions
# ==========================================================

# ZeroDivisionError
#
# 10 / 0


# ValueError
#
# int("abc")


# TypeError
#
# "5" + 10


# IndexError
#
# a = [1,2,3]
# print(a[5])


# KeyError
#
# d = {"name":"Ruchit"}
# print(d["age"])


# FileNotFoundError
#
# open("abc.txt")


# ==========================================================
# Exception vs Error
# ==========================================================

# Error
# -----
# Something went wrong in the program.
#
# Example:
# Division by zero.


# Exception
# ---------
# A specific type of runtime error that Python
# can handle using try-except.


# ==========================================================
# Keywords Summary
# ==========================================================

# try
# ----
# Write code that may produce an error.


# except
# -------
# Handles the error if one occurs.


# else
# ----
# Executes only when there is NO exception.


# finally
# -------
# Executes every time, whether an error occurs or not.


# raise
# -----
# Used to create and throw a custom exception.


# ==========================================================
# Quick Summary
# ==========================================================

# try
# → Check code for errors.
#
# except
# → Handle the error.
#
# else
# → Runs when no error occurs.
#
# finally
# → Always runs.
#
# raise
# → Create your own exception.
#
# Exception as err
# → Stores the error message in the variable 'err'.
#
# ==========================================================