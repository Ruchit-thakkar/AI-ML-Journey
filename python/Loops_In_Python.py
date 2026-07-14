# ==========================================================
#                    LOOPS IN PYTHON
# ==========================================================
#
# Description:
# Loops are used to perform repetitive tasks in Python.
# Instead of writing the same code multiple times, loops
# execute a block of code repeatedly.
#
# Types of Loops:
# 1. For Loop
# 2. While Loop
#
# For Loop:
# Used when you know how many times the loop should run.
#
# While Loop:
# Used when the loop depends on a condition.
#
# range(start, stop, step)
# start -> Starting value
# stop  -> Ending value (Excluded)
# step  -> Increment/Decrement
#
# Syntax:
# for i in range(start, stop, step):
#     print(i)
#
# ==========================================================


# =======================
# 1. FOR LOOP
# =======================
print("1. FOR LOOP")

for i in range(1, 11, 1):
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


# =======================
# 2. WHILE LOOP
# =======================
print("\n2. WHILE LOOP")

i = 1

while i <= 10:
    print(i)
    i += 1

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


# =======================
# 3. RANGE FUNCTION
# =======================
print("\n3. RANGE FUNCTION")

for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4


# =======================
# 4. RANGE WITH START, STOP, STEP
# =======================
print("\n4. RANGE (START, STOP, STEP)")

for i in range(1, 11, 2):
    print(i)

# Output:
# 1
# 3
# 5
# 7
# 9


# =======================
# 5. LOOP THROUGH STRING
# =======================
print("\n5. LOOP THROUGH STRING")

name = "Python"

for i in name:
    print(i)

# Output:
# P
# y
# t
# h
# o
# n


# =======================
# 6. STRING USING INDEX
# =======================
print("\n6. STRING USING INDEX")

name = "Python"

for i in range(len(name)):
    print(name[i])

# Output:
# P
# y
# t
# h
# o
# n


# ==========================================================
# PRACTICE PROGRAMS
# ==========================================================

# Practice 1
print("\nPractice 1 : Print numbers from 10 to 40")

for i in range(10, 41):
    print(i)

# Output:
# 10 11 12 ... 39 40


# Practice 2
print("\nPractice 2 : Print numbers from -10 to 20")

for i in range(-10, 21):
    print(i)

# Output:
# -10 -9 -8 ... 19 20


# Practice 3
print("\nPractice 3 : Print numbers from 34 to 5")

for i in range(34, 4, -1):
    print(i)

# Output:
# 34 33 32 ... 6 5


# ==========================================================
# COMMIT:
# Learned Python loops including For Loop, While Loop,
# range() function, looping through strings, using string
# indexes, and solving number printing practice problems.
# ==========================================================