"""
=========================================================
        PYTHON MODULES & PACKAGES - COMPLETE NOTES
=========================================================

Topics
------
1. What is a Module?
2. Creating a Module
3. Importing a Module
4. Different Ways to Import
5. Why Use Modules?
6. What is a Package?
7. Package Structure
8. Importing from a Package
9. Difference Between Module & Package
"""

# =====================================================
# 1. WHAT IS A MODULE?
# =====================================================

"""
A Module is simply a Python (.py) file.

A module can contain:
✔ Variables
✔ Functions
✔ Classes
✔ Executable Code

Purpose:
- Reuse code
- Organize programs
- Avoid writing the same code repeatedly

Example

calculator.py
--------------
PI = 3.14

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

class Calculator:
    pass
"""

# =====================================================
# 2. CREATING A MODULE
# =====================================================

"""
Step 1

Create a file

calculator.py

Step 2

Write code inside it.

Example

---------------- calculator.py ----------------

PI = 3.14

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

------------------------------------------------
"""

# =====================================================
# 3. USING (IMPORTING) A MODULE
# =====================================================

"""
Method 1

import calculator

Example

import calculator

print(calculator.PI)
print(calculator.add(10,20))

Output
------
3.14
30

Explanation
-----------
calculator.add()

means

Go inside calculator.py
Call function add()
"""

# =====================================================
# 4. IMPORT SPECIFIC FUNCTION
# =====================================================

"""
from calculator import add

print(add(50,30))

Output
------
80

Explanation
-----------
Only "add" is imported.

No need to write

calculator.add()
"""

# =====================================================
# 5. IMPORT MULTIPLE FUNCTIONS
# =====================================================

"""
from calculator import add, sub

print(add(5,5))
print(sub(10,2))

Output
------
10
8
"""

# =====================================================
# 6. IMPORT EVERYTHING
# =====================================================

"""
from calculator import *

print(add(4,6))
print(sub(10,5))

Output
------
10
5

NOTE
----
Avoid using *

Reason:
It may create name conflicts in large projects.
"""

# =====================================================
# 7. IMPORT WITH ALIAS
# =====================================================

"""
import calculator as cal

print(cal.add(5,10))

Output
------
15

Explanation

Alias means another short name.

calculator

becomes

cal
"""

# =====================================================
# 8. WHY USE MODULES?
# =====================================================

"""
Advantages

✔ Code Reuse
✔ Better Organization
✔ Easy Maintenance
✔ Easy Debugging
✔ Avoid Duplicate Code
"""

# =====================================================
# 9. WHAT IS A PACKAGE?
# =====================================================

"""
A Package is a folder containing multiple modules.

Traditional package structure:

mypackage/
    __init__.py
    math.py
    message.py

Older Python versions required __init__.py.
Modern Python can also use namespace packages, but
__init__.py is still commonly used.
"""

# =====================================================
# 10. PACKAGE STRUCTURE
# =====================================================

"""
Project/

│
├── main.py
│
└── mypackage/
      │
      ├── __init__.py
      ├── math.py
      └── message.py
"""

# =====================================================
# 11. FILES INSIDE PACKAGE
# =====================================================

"""
math.py

def square(n):
    return n*n

def cube(n):
    return n*n*n


------------------------------------


message.py

def hello():
    print("Welcome")


------------------------------------


__init__.py

print("Package Loaded")

(or it can be empty)
"""

# =====================================================
# 12. IMPORT MODULE FROM PACKAGE
# =====================================================

"""
import mypackage.math

print(mypackage.math.square(5))

Output
------
Package Loaded
25

Explanation

Python enters

mypackage

then opens

math.py

then calls

square()
"""

# =====================================================
# 13. IMPORT SPECIFIC FUNCTION FROM PACKAGE
# =====================================================

"""
from mypackage.math import cube

print(cube(3))

Output
------
27
"""

# =====================================================
# 14. IMPORT ANOTHER MODULE
# =====================================================

"""
from mypackage import message

message.hello()

Output
------
Package Loaded
Welcome
"""

# =====================================================
# 15. IMPORT PACKAGE USING ALIAS
# =====================================================

"""
import mypackage.math as m

print(m.square(8))

Output
------
64
"""

# =====================================================
# 16. MODULE vs PACKAGE
# =====================================================

"""
MODULE
------
Single Python (.py) file

Example

calculator.py


PACKAGE
-------
Folder containing multiple modules

Example

mypackage/

    math.py
    message.py
"""

# =====================================================
# 17. REAL PROJECT EXAMPLE
# =====================================================

"""
Student Management System

Project/

│
├── main.py
├── database.py
├── student.py
├── teacher.py
│
└── utils/
      │
      ├── __init__.py
      ├── email.py
      └── sms.py

database.py   -> Module

student.py    -> Module

teacher.py    -> Module

utils/        -> Package

email.py      -> Module

sms.py        -> Module
"""

# =====================================================
# 18. SUMMARY
# =====================================================

"""
Module
------
A single Python (.py) file.

Package
-------
A folder containing multiple modules.

Import Module
-------------
import module_name

Example

import calculator

Import Function
---------------
from module_name import function_name

Example

from calculator import add

Import Everything
-----------------
from module_name import *

Import Package Module
---------------------
import package_name.module_name

Example

import mypackage.math

Import with Alias
-----------------
import module_name as alias

Example

import calculator as cal

Key Difference
--------------
Module  = One Python file

Package = Folder containing multiple Python files
"""