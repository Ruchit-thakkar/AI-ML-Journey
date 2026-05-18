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


# =========================================================
# 2. VARIABLES
# =========================================================
# Variables are containers used to store data.

name = "Ruchit"
age = 20

# f-string is used to insert variables inside strings.
print(f"Name : {name} | Age : {age}")


# =========================================================
# 3. VARIABLE NAMING STYLES
# =========================================================

# Camel Case
# First word starts with lowercase,
# next words start with uppercase.
camelCase = 20

# Pascal Case
# Every word starts with uppercase.
PascalCase = 20

# Snake Case
# Words are separated using underscore (_)
snake_case = 20


# =========================================================
# 4. DATA TYPES
# =========================================================
# Python automatically detects the type of data.

# Integer -> whole numbers
a = 20
print(type(a))

# Float -> decimal numbers
a = 20.2
print(type(a))

# Complex Number
a = 20j
print(type(a))

# String -> text data
name = "Ruchit"
print(type(name))

# Boolean -> True or False
boolean = True
print(type(boolean))


# =========================================================
# 5. STRING INDEXING
# =========================================================
# Indexing is used to access single characters from a string.
# Index starts from 0.

name = "Ruchit"

print(name[0])   # R
print(name[1])   # u
print(name[2])   # c


# =========================================================
# 6. STRING SLICING
# =========================================================
# Slicing is used to access multiple characters.

# Syntax:
# string[start : stop : step]

name = "Ruchit"

print(name[0:4])      # Ruch
print(name[0:6:1])    # Ruchit
print(name[0:6:2])    # Rci
print(name[::-1])     # Reverse String


# =========================================================
# 7. ESCAPE SEQUENCES
# =========================================================
# Escape sequences are special characters.

# \n -> New Line
print("Hello\nRuchit")

# \t -> Tab Space
print("Hello\tRuchit")

# \\ -> Print Backslash
print("C:\\Users\\Ruchit")

# \" -> Double Quote inside string
print("My name is \"Ruchit\"")


# =========================================================
# 8. RAW STRING
# =========================================================
# Raw string ignores escape sequences.

print(r"C:\Users\Ruchit\Documents")


# =========================================================
# 9. TYPE CONVERSION
# =========================================================
# Convert one data type into another.

# int()
a = int("20")
print(a)

# float()
b = float(20)
print(b)

# str()
c = str(200)
print(type(c))

# bool()
d = bool(1)
print(d)


# =========================================================
# 10. TRUE VALUES AND FALSE VALUES
# =========================================================

# False Values:
# False, 0, 0.0, "", None, [], {}, ()

print(bool(0))
print(bool(""))
print(bool([]))

# True Values:
# Everything except false values.

print(bool(1))
print(bool("Ruchit"))
print(bool([1, 2, 3]))


# =========================================================
# 11. INPUT / OUTPUT
# =========================================================
# input() always takes data as string by default.

name = input("Enter your name : ")
age = int(input("Enter your age : "))

print(f"Welcome {name}")
print(f"Your age is {age}")


# =========================================================
# 12. ARITHMETIC OPERATORS
# =========================================================

a = 10
b = 3

print(a + b)   # Addition
print(a - b)   # Subtraction
print(a * b)   # Multiplication
print(a / b)   # Division
print(a // b)  # Floor Division
print(a % b)   # Modulus (Remainder)
print(a ** b)  # Power


# =========================================================
# 13. STRING CONCATENATION
# =========================================================
# + is used to join strings.

first_name = "Ruchit"
last_name = "Thakkar"

full_name = first_name + " " + last_name

print(full_name)


# =========================================================
# 14. STRING MULTIPLICATION
# =========================================================
# * is used to repeat strings.

print("AI " * 5)


# =========================================================
# 15. COMPARISON OPERATORS
# =========================================================
# Result is always True or False.

a = 10
b = 20

print(a == b)   # Equal
print(a != b)   # Not Equal
print(a > b)    # Greater Than
print(a < b)    # Less Than
print(a >= b)   # Greater Than Equal To
print(a <= b)   # Less Than Equal To


# =========================================================
# 16. LOGICAL OPERATORS
# =========================================================
# and -> Both conditions must be True
# or  -> At least one condition must be True
# not -> Reverse the result

age = 20

print(age > 18 and age < 30)
print(age > 18 or age < 10)
print(not(age > 18))


# =========================================================
# 17. IF ELSE CONDITIONS
# =========================================================

age = int(input("Enter your age : "))

if age >= 18:
    print("You can vote")

else:
    print("You cannot vote")


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


# =========================================================
# 19. LOOPS
# =========================================================
# Loops are used to perform repetitive tasks.

# Types of loops:
# 1. For Loop
# 2. While Loop


# =========================================================
# 20. FOR LOOP WITH RANGE()
# =========================================================
# range(start, stop, step)

for i in range(1, 11):
    print(i)


# =========================================================
# 21. FOR LOOP WITH STRING
# =========================================================

name = "Ruchit"

for character in name:
    print(character)


# =========================================================
# 22. FOR LOOP WITH len() AND INDEXING
# =========================================================

name = "Ruchit"

for i in range(len(name)):
    print(f"Index : {i} | Character : {name[i]}")


# =========================================================
# 23. WHILE LOOP
# =========================================================
# While loop runs until condition becomes False.

count = 1

while count <= 5:
    print(count)
    count += 1


# =========================================================
# 24. PRACTICE QUESTIONS
# =========================================================

# Print numbers from 10 to 40
print("Numbers from 10 to 40")

for i in range(10, 41):
    print(i)


# Print numbers from -10 to 20
print("Numbers from -10 to 20")

for i in range(-10, 21):
    print(i)


# Print numbers from 34 to 5
print("Numbers from 34 to 5")

for i in range(34, 4, -1):
    print(i)


# =========================================================
# END OF DAY 1
# =========================================================