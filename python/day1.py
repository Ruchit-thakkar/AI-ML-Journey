# =========================================================
# PYTHON BASICS - DAY 1
# AI / ML Journey by Ruchit
# =========================================================


# =========================================================
# 1. PRINT FUNCTION
# =========================================================
# print() is used to display output on the screen.

print("Hello Ruchit")
print("Day 1 of AI-ML-Journey")

# Output:
# Hello Ruchit
# Day 1 of AI-ML-Journey



# =========================================================
# 2. VARIABLES
# =========================================================
# Variables are containers used to store data.

name = "Ruchit"
age = 20

# f-string is used to insert variables inside strings.
print(f"Name : {name} | Age : {age}")

# Output:
# Name : Ruchit | Age : 20



# =========================================================
# 3. VARIABLE NAMING STYLES
# =========================================================

# Camel Case
camelCase = 20

# Pascal Case
PascalCase = 20

# Snake Case
snake_case = 20

print(camelCase)
print(PascalCase)
print(snake_case)

# Output:
# 20
# 20
# 20



# =========================================================
# 4. DATA TYPES
# =========================================================
# Python automatically detects the type of data.

# Integer -> whole numbers
a = 20
print(type(a))

# Output:
# <class 'int'>


# Float -> decimal numbers
a = 20.2
print(type(a))

# Output:
# <class 'float'>


# Complex Number
a = 20j
print(type(a))

# Output:
# <class 'complex'>


# String -> text data
name = "Ruchit"
print(type(name))

# Output:
# <class 'str'>


# Boolean -> True or False
boolean = True
print(type(boolean))

# Output:
# <class 'bool'>



# =========================================================
# 5. STRING INDEXING
# =========================================================
# Indexing is used to access single characters from a string.

name = "Ruchit"

print(name[0])
print(name[1])
print(name[2])

# Output:
# R
# u
# c



# =========================================================
# 6. STRING SLICING
# =========================================================
# Slicing is used to access multiple characters.

name = "Ruchit"

print(name[0:4])
print(name[0:6:1])
print(name[0:6:2])
print(name[::-1])

# Output:
# Ruch
# Ruchit
# Rci
# tihcuR



# =========================================================
# 7. ESCAPE SEQUENCES
# =========================================================

# \n -> New Line
print("Hello\nRuchit")

# Output:
# Hello
# Ruchit


# \t -> Tab Space
print("Hello\tRuchit")

# Output:
# Hello    Ruchit


# \\ -> Print Backslash
print("C:\\Users\\Ruchit")

# Output:
# C:\Users\Ruchit


# \" -> Double Quote inside string
print("My name is \"Ruchit\"")

# Output:
# My name is "Ruchit"



# =========================================================
# 8. RAW STRING
# =========================================================
# Raw string ignores escape sequences.

print(r"C:\Users\Ruchit\Documents")

# Output:
# C:\Users\Ruchit\Documents



# =========================================================
# 9. TYPE CONVERSION
# =========================================================

# int()
a = int("20")
print(a)

# Output:
# 20


# float()
b = float(20)
print(b)

# Output:
# 20.0


# str()
c = str(200)
print(type(c))

# Output:
# <class 'str'>


# bool()
d = bool(1)
print(d)

# Output:
# True



# =========================================================
# 10. TRUE VALUES AND FALSE VALUES
# =========================================================

# False Values
print(bool(0))
print(bool(""))
print(bool([]))

# Output:
# False
# False
# False


# True Values
print(bool(1))
print(bool("Ruchit"))
print(bool([1, 2, 3]))

# Output:
# True
# True
# True



# =========================================================
# 11. INPUT / OUTPUT
# =========================================================
# input() always takes data as string.

name = input("Enter your name : ")
age = int(input("Enter your age : "))

print(f"Welcome {name}")
print(f"Your age is {age}")

# Example Input:
# Ruchit
# 20

# Output:
# Welcome Ruchit
# Your age is 20



# =========================================================
# 12. ARITHMETIC OPERATORS
# =========================================================

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

# Output:
# 13
# 7
# 30
# 3.3333333333333335
# 3
# 1
# 1000



# =========================================================
# 13. STRING CONCATENATION
# =========================================================

first_name = "Ruchit"
last_name = "Thakkar"

full_name = first_name + " " + last_name

print(full_name)

# Output:
# Ruchit Thakkar



# =========================================================
# 14. STRING MULTIPLICATION
# =========================================================

print("AI " * 5)

# Output:
# AI AI AI AI AI



# =========================================================
# 15. COMPARISON OPERATORS
# =========================================================

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

# Output:
# False
# True
# False
# True
# False
# True



# =========================================================
# 16. LOGICAL OPERATORS
# =========================================================

age = 20

print(age > 18 and age < 30)
print(age > 18 or age < 10)
print(not(age > 18))

# Output:
# True
# True
# False



# =========================================================
# 17. IF ELSE CONDITIONS
# =========================================================

age = int(input("Enter your age : "))

if age >= 18:
    print("You can vote")

else:
    print("You cannot vote")

# Example Input:
# 20

# Output:
# You can vote



# =========================================================
# 18. ELIF STATEMENT
# =========================================================

marks = int(input("Enter your marks : "))

if marks >= 90:
    print("Grade A")

elif marks >= 70:
    print("Grade B")

elif marks >= 50:
    print("Grade C")

else:
    print("Fail")

# Example Input:
# 85

# Output:
# Grade B



# =========================================================
# 19. LOOPS
# =========================================================
# Loops are used to perform repetitive tasks.



# =========================================================
# 20. FOR LOOP WITH RANGE()
# =========================================================

for i in range(1, 11):
    print(i)

# Output:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10



# =========================================================
# 21. FOR LOOP WITH STRING
# =========================================================

name = "Ruchit"

for character in name:
    print(character)

# Output:
# R
# u
# c
# h
# i
# t



# =========================================================
# 22. FOR LOOP WITH len() AND INDEXING
# =========================================================

name = "Ruchit"

for i in range(len(name)):
    print(f"Index : {i} | Character : {name[i]}")

# Output:
# Index : 0 | Character : R
# Index : 1 | Character : u
# Index : 2 | Character : c
# Index : 3 | Character : h
# Index : 4 | Character : i
# Index : 5 | Character : t



# =========================================================
# 23. WHILE LOOP
# =========================================================

count = 1

while count <= 5:
    print(count)
    count += 1

# Output:
# 1
# 2
# 3
# 4
# 5



# =========================================================
# 24. PRACTICE QUESTIONS
# =========================================================

# Print numbers from 10 to 40
print("Numbers from 10 to 40")

for i in range(10, 41):
    print(i)

# Output:
# 10 to 40



# Print numbers from -10 to 20
print("Numbers from -10 to 20")

for i in range(-10, 21):
    print(i)

# Output:
# -10 to 20



# Print numbers from 34 to 5
print("Numbers from 34 to 5")

for i in range(34, 4, -1):
    print(i)

# Output:
# 34 to 5



# =========================================================
# END OF DAY 1
# =========================================================