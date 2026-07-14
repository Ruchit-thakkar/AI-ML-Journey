# ==========================================================
#            CONDITIONAL STATEMENTS IN PYTHON
# ==========================================================
#
# Description:
# Conditional statements are used to control the flow of a
# program. They execute different blocks of code based on
# whether a condition is True or False.
#
# Topics Covered:
# 1. if Statement
# 2. if-else Statement
# 3. elif Statement
# 4. Logical Operators (and, or, not)
# 5. pass Statement
# 6. Ternary Operator
# 7. Greatest of Three Numbers
#
# ==========================================================


# =======================
# 1. IF STATEMENT
# =======================
print("1. IF STATEMENT")

a = 10

if a > 5:
    print("a is greater than 5")

# Output:
# 1. IF STATEMENT
# a is greater than 5


# =======================
# 2. IF ELSE
# =======================
print("\n2. IF ELSE")

age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")

# Output:
# 2. IF ELSE
# Not Eligible to Vote


# =======================
# 3. ELIF STATEMENT
# =======================
print("\n3. ELIF STATEMENT")

marks = 72

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")

# Output:
# 3. ELIF STATEMENT
# Grade C


# =======================
# 4. LOGICAL OPERATORS
# =======================
print("\n4. LOGICAL OPERATORS")

# AND Operator
age = 20
citizen = True

if age >= 18 and citizen:
    print("AND : Eligible to Vote")

# OR Operator
a = 5
b = 10

if a == 5 or b == 20:
    print("OR : Condition is True")

# NOT Operator
is_raining = False

if not is_raining:
    print("NOT : Go Outside")

# Output:
# 4. LOGICAL OPERATORS
# AND : Eligible to Vote
# OR : Condition is True
# NOT : Go Outside


# =======================
# 5. PASS STATEMENT
# =======================
print("\n5. PASS STATEMENT")

x = 10

if x > 5:
    pass
else:
    print("Small Number")

print("Pass Statement Executed Successfully")

# Output:
# 5. PASS STATEMENT
# Pass Statement Executed Successfully


# =======================
# 6. TERNARY OPERATOR
# =======================
print("\n6. TERNARY OPERATOR")

a = 10
b = 10

print("Result :", "True" if a == b else "False")

num = 8
print("Number is", "Even" if num % 2 == 0 else "Odd")

# Output:
# 6. TERNARY OPERATOR
# Result : True
# Number is Even


# =======================
# 7. GREATEST OF THREE NUMBERS
# =======================
print("\n7. GREATEST OF THREE NUMBERS")

A = 12
B = 24
C = 20

if A > B and A > C:
    print("A is Greater =", A)
elif B > A and B > C:
    print("B is Greater =", B)
else:
    print("C is Greater =", C)

# Output:
# 7. GREATEST OF THREE NUMBERS
# B is Greater = 24


# ==========================================================
# COMMIT:
# Learned Python Conditional Statements including if, else,
# elif, logical operators (and, or, not), pass statement,
# ternary operator, and finding the greatest of three numbers.
# ==========================================================
