# ==========================================
# Python Arithmetic Operators
# ==========================================

# (+) Addition Operator
# Adds two numbers together.

a = 12
b = 13

print(a + b)      # Output: 25


# ------------------------------------------

# (-) Subtraction Operator
# Subtracts the second number from the first.

a = 12
b = 13

print(a - b)      # Output: -1


# ------------------------------------------

# (*) Multiplication Operator
# Multiplies two numbers.

a = 12
b = 13

print(a * b)      # Output: 156


# ------------------------------------------

# (/) Division Operator
# Returns the exact quotient as a float (decimal).

a = 22
b = 7

print(a / b)      # Output: 3.142857142857143


# ------------------------------------------

# (//) Floor Division Operator
# Returns only the integer part of the division.
# The decimal part is removed.

a = 22
b = 7

print(a // b)     # Output: 3


# ------------------------------------------

# (**) Exponent Operator
# Raises the first number to the power of the second.

a = 2
b = 3

print(a ** b)     # Output: 8
                  # 2 × 2 × 2 = 8


# ------------------------------------------

# (%) Modulus Operator
# Returns the remainder after division.

a = 22
b = 7

print(a % b)      # Output: 1
                  # 22 ÷ 7 = 3 remainder 1


# ------------------------------------------

# (+) cannot add a string and an integer.

# print("hello " + 10)
# Output:
# TypeError: can only concatenate str (not "int") to str

# Correct way:
# print("hello " + str(10))
# Output: hello 10


# ------------------------------------------

# (*) String Multiplication
# Repeats the string multiple times.

print("hello " * 10)

# Output:
# hello hello hello hello hello hello hello hello hello hello



# ==========================================
# Assignment Operators
# ==========================================

# (=) Assignment Operator
a = 10
print(a)          # Output: 10

# ------------------------------------------

# (+=) Add and Assign
a = 10
a += 5
print(a)          # Output: 15

# ------------------------------------------

# (-=) Subtract and Assign
a = 10
a -= 5
print(a)          # Output: 5

# ------------------------------------------

# (*=) Multiply and Assign
a = 10
a *= 5
print(a)          # Output: 50

# ------------------------------------------

# (/=) Divide and Assign
a = 10
a /= 5
print(a)          # Output: 2.0

# ------------------------------------------

# (%=) Modulus and Assign
a = 22
a %= 7
print(a)          # Output: 1

# ------------------------------------------

# (//=) Floor Divide and Assign
a = 22
a //= 7
print(a)          # Output: 3


# ==========================================
# Comparison Operators
# ==========================================

# (==) Equal To
a = 10
b = 10
print(a == b)      # Output: True

# ------------------------------------------

# (!=) Not Equal To
a = 10
b = 5
print(a != b)      # Output: True

# ------------------------------------------

# (>) Greater Than
a = 10
b = 5
print(a > b)       # Output: True

# ------------------------------------------

# (<) Less Than
a = 10
b = 5
print(a < b)       # Output: False

# ------------------------------------------

# (>=) Greater Than or Equal To
a = 10
b = 10
print(a >= b)      # Output: True

# ------------------------------------------

# (<=) Less Than or Equal To
a = 10
b = 5
print(a <= b)      # Output: False


# ==========================================
# Logical Operators
# ==========================================

# (and) Logical AND
# Returns True if both conditions are True.

a = 10
b = 5
print(a > b and a < 20)      # Output: True

# ------------------------------------------

# (or) Logical OR
# Returns True if at least one condition is True.

a = 10
b = 5
print(a < b or a == 10)      # Output: True

# ------------------------------------------

# (not) Logical NOT
# Reverses the Boolean result.

a = 10
print(not(a == 10))          # Output: False




# ==========================================
# Program: Total Items Calculation
# ==========================================

# Take input from the user
price = float(input("Enter price of one item: "))
quantity = int(input("Enter number of items: "))

# Calculate total cost
total = price * quantity

# Display the result
print(f"Total Amount to Pay ₹{total:,.2f}")





# ==========================================
# Program: Candies per Kid
# ==========================================

# Take input from the user
candies = int(input("Enter total number of candies: "))
kids = int(input("Enter total number of kids: "))

# Calculate candies per kid
candies_per_kid = candies // kids

# Calculate remaining candies
remaining_candies = candies % kids

# Display the result
print(f"Candies per Kid = {candies_per_kid}")
print(f"Remaining Candies = {remaining_candies}")