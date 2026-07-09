#Comments

#single line using

"""Multiline 
Comments 
using"""

print("Hello World")

a=12
b=13
print(a+b)

#3 types 
# camel case - 
helloWorId=67
#pascal case
HelloWorld=67
#Snake case
hello_world=67
#We can use any type in python
#You cannot start a variable with a number
#You cannot use spaces in variable
#You cannot use special characters in variable exception (_)

#Data types
a=12
b=12.34
c=2j
d="Hello World"
#or 
e='Hello World'
f=True
g=False
print(type(a),a)
print(type(b),b)
print(type(c),c)
print(type(d),d)
print(type(e),e)
print(type(f),f)
print(type(g),g)

#Integers are numbers (to infinity... -3 ,-2 ,-1 ,O, 1, 2 ... to infinity)
#Float are number which have numbers with decimal point and
#fraction value.
#Complex are the numbers with imaginary values
#Strings can contain any values, characters and everything
#Boolean will only return True and False

# ==========================================
# Python Strings - In Depth
# ==========================================

# Create a string
d = "hello"

# ------------------------------------------
# String Indexing
# ------------------------------------------

print("h e l l o")
print("0 1 2 3 4")

# Output:
# h e l l o
# 0 1 2 3 4

print("h e l l o")
print("-5 -4 -3 -2 -1")

# Output:
# h e l l o
# -5 -4 -3 -2 -1

# Access characters using positive indexing
print(d[0])  # h
print(d[1])  # e
print(d[2])  # l
print(d[3])  # l
print(d[4])  # o

# Output:
# h
# e
# l
# l
# o

# ------------------------------------------
# String Slicing
# Syntax: string[start:stop:step]
# ------------------------------------------

a = "yoo brother"

print("String Slicing")
print("Syntax: string[start:stop:step]")

# Output:
# String Slicing
# Syntax: string[start:stop:step]

print(a[0:8:1])  # yoo brot
print(a[0:8:2])  # yort
print(a[0:8:3])  # y t
print(a[0:8:4])  # yr

# Output:
# yoo brot
# yort
# y t
# yr

# ------------------------------------------
# String Concatenation
# ------------------------------------------

print("Hello " + "my name is " + "Ruchit")
print("Hello" + " my name is " + "Ruchit")

# Output:
# Hello my name is Ruchit
# Hello my name is Ruchit

# Using commas in print()
print("Hello", "My name is", "Ruchit")

# Output:
# Hello My name is Ruchit

# ------------------------------------------
# f-Strings
# ------------------------------------------

name = "Ruchit"

print(f"Hello my name is {name}")

# Output:
# Hello my name is Ruchit

# ------------------------------------------
# Escape Characters
# ------------------------------------------

print(f"Hello my name is {name}\nI am from\tIndia")

# Output:
# Hello my name is Ruchit
# I am from    India

# ------------------------------------------
# Raw String
# ------------------------------------------

print(r"Hello my name is \b {name}\nI am from \t India")

# Output:
# Hello my name is \b {name}\nI am from \t India