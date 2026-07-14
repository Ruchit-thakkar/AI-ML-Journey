# ==========================================================
#            INTRODUCTION TO DATA STRUCTURES
# ==========================================================
#
# Description:
# A Data Structure is a way of storing and organizing data
# so that it can be accessed and modified efficiently.
#
# Data Structures allow us to store multiple values in a
# single variable instead of creating many separate variables.
#
# Types of Data Structures:
#
# 1. In-built Data Structures
#    - List
#    - Tuple
#    - Set
#    - Dictionary
#
# 2. Customized Data Structures
#    - Stack
#    - Queue
#    - Linked List
#    - Trees
#    - Graphs
#
# In this course, we will mainly study Python's
# In-built Data Structures.
#
# ==========================================================


# =======================
# 1. LIST
# =======================
print("----- LIST -----")

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits)

# Output:
# ['Apple', 'Banana', 'Mango', 'Orange']


# =======================
# 2. TUPLE
# =======================
print("\n----- TUPLE -----")

numbers = (10, 20, 30, 40)

print(numbers)

# Output:
# (10, 20, 30, 40)


# =======================
# 3. SET
# =======================
print("\n----- SET -----")

colors = {"Red", "Green", "Blue"}

print(colors)

# Output:
# {'Red', 'Green', 'Blue'}
# (Order may vary)


# =======================
# 4. DICTIONARY
# =======================
print("\n----- DICTIONARY -----")

student = {
    "Name": "Ruchit",
    "Age": 19,
    "City": "Ahmedabad"
}

print(student)

# Output:
# {'Name': 'Ruchit', 'Age': 19, 'City': 'Ahmedabad'}


# ==========================================================
# SUMMARY OF DATA STRUCTURES
# ==========================================================
#
# List
# - Ordered
# - Mutable (Can be Changed)
# - Allows Duplicate Values
#
# Tuple
# - Ordered
# - Immutable (Cannot be Changed)
# - Allows Duplicate Values
#
# Set
# - Unordered
# - Mutable
# - No Duplicate Values
#
# Dictionary
# - Stores data as Key : Value pairs
# - Mutable
# - Keys must be Unique
#
# ==========================================================


# ==========================================================
# COMMIT:
# Learned the introduction to Data Structures, their purpose,
# types (In-built and Customized), and explored Python's
# in-built data structures: List, Tuple, Set, and Dictionary.
# ==========================================================
# ==========================================================
#               INTRODUCTION TO DICTIONARY
# ==========================================================
#
# Description:
# A Dictionary is an in-built data structure used to store
# multiple values in the form of Key : Value pairs.
#
# Features:
# • Uses {} (Curly Braces)
# • Stores data as Key : Value pairs
# • Mutable (Can be Modified)
# • Maintains insertion order (Python 3.7+)
# • Duplicate Keys are NOT allowed
# • Duplicate Values are Allowed
#
# Syntax:
# dictionary_name = {
#     key1 : value1,
#     key2 : value2
# }
#
# ==========================================================


# =======================
# 1. CREATE A DICTIONARY
# =======================
print("----- CREATE DICTIONARY -----")

student = {
    "Name": "Ruchit",
    "Age": 19,
    "City": "Ahmedabad"
}

print(student)

# Output:
# {'Name': 'Ruchit', 'Age': 19, 'City': 'Ahmedabad'}


# =======================
# 2. ACCESS VALUES
# =======================
print("\n----- ACCESS VALUES -----")

print(student["Name"])
print(student["Age"])

# Output:
# Ruchit
# 19


# =======================
# 3. USING dict() CONSTRUCTOR
# =======================
print("\n----- dict() CONSTRUCTOR -----")

employee = dict(Name="Rahul", Age=25, City="Surat")

print(employee)

# Output:
# {'Name': 'Rahul', 'Age': 25, 'City': 'Surat'}


# ==========================================================
# DICTIONARY TRAVERSING
# ==========================================================

# =======================
# 4. TRAVERSE USING KEYS
# =======================
print("\n----- TRAVERSE USING KEYS -----")

for key in student:
    print(key)

# Output:
# Name
# Age
# City


# =======================
# 5. TRAVERSE USING VALUES
# =======================
print("\n----- TRAVERSE USING VALUES -----")

for value in student.values():
    print(value)

# Output:
# Ruchit
# 19
# Ahmedabad


# =======================
# 6. TRAVERSE USING KEYS & VALUES
# =======================
print("\n----- KEYS AND VALUES -----")

for key, value in student.items():
    print(key, ":", value)

# Output:
# Name : Ruchit
# Age : 19
# City : Ahmedabad


# ==========================================================
# DICTIONARY METHODS
# ==========================================================

student = {
    "Name": "Ruchit",
    "Age": 19,
    "City": "Ahmedabad"
}


# =======================
# 7. keys()
# =======================
print("\n----- keys() -----")

print(student.keys())

# Output:
# dict_keys(['Name', 'Age', 'City'])


# =======================
# 8. values()
# =======================
print("\n----- values() -----")

print(student.values())

# Output:
# dict_values(['Ruchit', 19, 'Ahmedabad'])


# =======================
# 9. items()
# =======================
print("\n----- items() -----")

print(student.items())

# Output:
# dict_items([('Name', 'Ruchit'),
#             ('Age', 19),
#             ('City', 'Ahmedabad')])


# =======================
# 10. get()
# =======================
print("\n----- get() -----")

print(student.get("Name"))

# Output:
# Ruchit


# =======================
# 11. update()
# =======================
print("\n----- update() -----")

student.update({"Age": 20})

print(student)

# Output:
# {'Name': 'Ruchit', 'Age': 20, 'City': 'Ahmedabad'}


# =======================
# 12. pop()
# =======================
print("\n----- pop() -----")

student.pop("City")

print(student)

# Output:
# {'Name': 'Ruchit', 'Age': 20}


# =======================
# 13. clear()
# =======================
print("\n----- clear() -----")

temp = {"A": 1, "B": 2}

temp.clear()

print(temp)

# Output:
# {}


# ==========================================================
# IMPORTANT NOTES
# ==========================================================
#
# Dictionary:
# • Stores data in Key : Value pairs.
# • Mutable (Can be Modified).
# • Duplicate Keys are NOT allowed.
# • Duplicate Values are allowed.
# • Traversing can be done using:
#     - keys()
#     - values()
#     - items()
#
# Common Methods:
# • keys()
# • values()
# • items()
# • get()
# • update()
# • pop()
# • clear()
#
# ==========================================================


# ==========================================================
# COMMIT:
# Learned Python Dictionary, dictionary creation, dict()
# constructor, accessing values, dictionary traversing using
# keys, values and items, and commonly used dictionary
# methods such as keys(), values(), items(), get(),
# update(), pop(), and clear().
# ==========================================================