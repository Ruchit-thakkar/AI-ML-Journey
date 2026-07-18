"""
====================================================
            PYTHON OOPS (Object Oriented Programming)
====================================================

Topics Covered
1. Class
2. Object
3. Class Variable
4. Instance Variable
5. Constructor (__init__)
6. self keyword
7. Methods
8. Static Method
9. Class Method
10. Inheritance
11. Multiple Inheritance
12. Dunder Methods
13. Abstract Class & Abstract Method
"""

# ====================================================
# 1. CLASS & OBJECT
# ====================================================

"""
Class
-----
A class is a blueprint for creating objects.

Object
------
An object is an instance of a class.

Syntax:
class ClassName:
    pass

obj = ClassName()
"""

class Factory:
    a = 12          # Class Variable

    def hello():
        print("Hello")

print("Factory.a =", Factory.a)
Factory.hello()

"""
Output
------
Factory.a = 12
Hello

Explanation
-----------
Factory.a
Accesses the class variable directly.

Factory.hello()
Calls the method without creating an object because
it has no 'self' parameter.
"""


# ====================================================
# 2. OBJECT AND SELF
# ====================================================

class Factory:

    name = "Ruchit"

    def hello(self):
        print(f"Hello, My name is {self.name}")

obj = Factory()

print(obj.name)
obj.hello()

"""
Output
------
Ruchit
Hello, My name is Ruchit

Explanation
-----------
self represents the current object.

obj.hello()

Internally Python converts it to

Factory.hello(obj)
"""


# ====================================================
# 3. CONSTRUCTOR (__init__)
# ====================================================

"""
Constructor

__init__()

Automatically executes when an object is created.
Used for initializing object data.
"""

class Factory:

    def __init__(self, material, zip, pockets):

        self.material = material
        self.zip = zip
        self.pockets = pockets

    def display(self):
        print(self.material, self.zip, self.pockets)

obj = Factory("Leather", 3, 3)

print(obj.material)
print(obj.zip)
print(obj.pockets)

obj.display()

"""
Output
------
Leather
3
3
Leather 3 3

Explanation
-----------
Factory("Leather",3,3)

Python automatically executes

__init__()

and stores the values inside the object.
"""


# ====================================================
# 4. NORMAL METHOD
# ====================================================

class Demo:

    language = "Python"

    def normal_method(self):
        print("Normal Method")
        print(self.language)

obj = Demo()
obj.normal_method()

"""
Output
------
Normal Method
Python

Explanation
-----------
Normal methods require an object.
"""


# ====================================================
# 5. STATIC METHOD
# ====================================================

class Demo:

    @staticmethod
    def static_method():
        print("Static Method")

Demo.static_method()

"""
Output
------
Static Method

Explanation
-----------
Static methods

✔ don't need self
✔ don't need cls
✔ cannot access instance variables directly

Used for utility functions.
"""


# ====================================================
# 6. CLASS METHOD
# ====================================================

class Demo:

    language = "Python"

    @classmethod
    def class_method(cls):
        print("Class Method")
        print(cls.language)

Demo.class_method()

"""
Output
------
Class Method
Python

Explanation
-----------
cls represents the class itself.

Used for modifying/accessing class variables.
"""


# ====================================================
# Difference Between Methods
# ====================================================

"""
Normal Method
-------------
Parameter : self
Works on : Object

Static Method
-------------
Parameter : None
Works on : Nothing

Class Method
------------
Parameter : cls
Works on : Class
"""


# ====================================================
# 7. INHERITANCE
# ====================================================

"""
Inheritance

Child class can reuse Parent class properties.

Animal
   ↑
 Human
"""

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}")
        print(f"Age  : {self.age}")

class Human(Animal):

    def __init__(self, name, age, number, group):

        super().__init__(name, age)

        self.number = number
        self.group = group

obj1 = Animal("Lion", 23)

obj2 = Human(
    "Ruchit",
    20,
    1234567890,
    "B+"
)

obj1.display()

print()

obj2.display()

print(obj2.number)
print(obj2.group)

"""
Output
------
Name : Lion
Age  : 23

Name : Ruchit
Age  : 20
1234567890
B+

Explanation
-----------
super()

Calls the constructor of the parent class.

Human gets

✔ name
✔ age
✔ display()

from Animal.
"""


# ====================================================
# Types of Inheritance
# ====================================================

"""
1. Single

A → B

2. Multiple

A
 \
  C
 /
B

3. Multilevel

A
↓
B
↓
C

4. Hierarchical

      A
     / \
    B   C

5. Hybrid
Combination of multiple types.
"""


# ====================================================
# 8. MULTIPLE INHERITANCE
# ====================================================

class Father:

    def house(self):
        print("Father House")

class Mother:

    def jewelry(self):
        print("Mother Jewelry")

class Child(Father, Mother):

    pass

obj = Child()

obj.house()
obj.jewelry()

"""
Output
------
Father House
Mother Jewelry

Explanation
-----------
Child inherits from both Father and Mother.
"""


# ====================================================
# 9. DUNDER METHODS
# ====================================================

"""
Dunder = Double Underscore

Examples

__init__()

__str__()

__len__()

__add__()

__repr__()

They are special methods automatically called by Python.
"""

class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Student : {self.name}"

obj = Student("Ruchit")

print(obj)

"""
Output
------
Student : Ruchit

Explanation
-----------
Normally

print(obj)

prints memory address.

After defining __str__()

Python prints custom text.
"""


# ====================================================
# 10. ABSTRACT CLASS
# ====================================================

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):

    def sound(self):
        print("Bark")

obj = Dog()
obj.sound()

"""
Output
------
Bark

Explanation
-----------
Abstract Class

Cannot create object directly.

Animal()

❌ Error

Dog()

✔ Works because it implements sound().
"""


# ====================================================
# SUMMARY
# ====================================================

"""
Class
-----
Blueprint

Object
------
Instance of class

self
----
Current object

cls
---
Current class

__init__
--------
Constructor

@staticmethod
-------------
No self
No cls

@classmethod
------------
Uses cls

Inheritance
-----------
Reuse parent properties

super()
-------
Calls parent constructor

Multiple Inheritance
--------------------
One child inherits multiple parents

Dunder Methods
--------------
Special built-in methods

Abstract Class
--------------
Cannot create object directly

Abstract Method
---------------
Must be implemented by child class.
"""