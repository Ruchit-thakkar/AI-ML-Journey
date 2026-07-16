# ==========================================================
# PYTHON NOTES - File Handling
# ==========================================================

# ----------------------------------------------------------
# What is File Handling?
# ----------------------------------------------------------
#
# File handling allows a Python program to:
#
# ✔ Read data from a file
# ✔ Write data into a file
# ✔ Append (add) data to an existing file
# ✔ Create new files
#
# Python provides the built-in open() function for working
# with files.


# ==========================================================
# open() Function
# ==========================================================
#
# Syntax:
#
# open(filename, mode)
#
# filename -> Name of the file
# mode     -> Operation to perform
#
# Example:
#
# open("test.txt", "r")


# ==========================================================
# File Modes
# ==========================================================
#
# "r"  -> Read (Default)
# "w"  -> Write (Creates new file or overwrites existing file)
# "a"  -> Append (Adds data to the end of file)
# "x"  -> Create new file (Error if file already exists)
# "rb" -> Read Binary
# "wb" -> Write Binary


# ==========================================================
# 1. Read File
# ==========================================================

# Open file in read mode

fs = open("test.txt", "r")

# Read complete file
print(fs.read())

# Always close the file after using it
fs.close()

# Example:
#
# test.txt
# -------------------
# Hello Python
# Welcome to File Handling
#
# Output:
#
# Hello Python
# Welcome to File Handling
#
# Explanation:
# open() opens the file.
# read() reads the complete file.
# close() closes the file.


print("--------------------------------")


# ==========================================================
# 2. Write File
# ==========================================================

# Open file in write mode

fs = open("t2.txt", "w")

fs.write("Test to File Handling Writing")

fs.close()

# Output:
#
# t2.txt
#
# Test to File Handling Writing
#
#
# Explanation:
#
# If the file doesn't exist:
# → Python creates it.
#
# If the file already exists:
# → All previous data is deleted.
#
# Write mode always starts with an empty file.


print("--------------------------------")


# ==========================================================
# 3. Append File
# ==========================================================

# Open file in append mode

fs = open("t2.txt", "a")

fs.write(" and my name is Ruchit")

fs.close()

# Output:
#
# Test to File Handling Writing and my name is Ruchit
#
#
# Explanation:
#
# Append mode DOES NOT remove old data.
#
# It adds new data at the end.


print("--------------------------------")


# ==========================================================
# 4. with open()
# ==========================================================

# Best and recommended way

with open("test.txt", "r") as fs:
    print(fs.read())

# Output:
#
# Contents of test.txt
#
#
# Explanation:
#
# with automatically:
#
# ✔ Opens the file
# ✔ Executes the code
# ✔ Closes the file automatically
#
# No need to call:
#
# fs.close()


print("--------------------------------")


# ==========================================================
# Difference Between "w" and "a"
# ==========================================================

# Write Mode ("w")
#
# Existing Data:
# Deleted
#
# Example:
#
# Before:
# Hello World
#
# Write:
# Python
#
# After:
# Python


# Append Mode ("a")
#
# Existing Data:
# Kept
#
# Example:
#
# Before:
# Hello World
#
# Append:
# Python
#
# After:
# Hello WorldPython
#
# (Use "\n" if you want the new text on the next line.)


print("--------------------------------")


# ==========================================================
# Common File Methods
# ==========================================================

# read()
# -------
# Reads the complete file.
#
# Example:
#
# fs.read()


# readline()
# ----------
# Reads only one line.
#
# Example:
#
# fs.readline()


# readlines()
# -----------
# Reads all lines and returns them as a list.
#
# Example:
#
# fs.readlines()


# write()
# -------
# Writes data into a file.
#
# Example:
#
# fs.write("Hello")


# close()
# -------
# Closes the file.
#
# Example:
#
# fs.close()


print("--------------------------------")


# ==========================================================
# Example of readline()
# ==========================================================

# Suppose test.txt contains:
#
# Apple
# Mango
# Banana

fs = open("test.txt", "r")

print(fs.readline())
print(fs.readline())

fs.close()

# Output:
#
# Apple
#
# Mango


print("--------------------------------")


# ==========================================================
# Example of readlines()
# ==========================================================

fs = open("test.txt", "r")

print(fs.readlines())

fs.close()

# Output:
#
# ['Apple\n', 'Mango\n', 'Banana']


print("--------------------------------")


# ==========================================================
# Why use "with"?
# ==========================================================

# Without with
#
# fs = open(...)
# ...
# fs.close()
#
# If an error occurs before close(),
# the file may remain open.


# With with
#
# with open(...) as fs:
#     ...
#
# Even if an error occurs,
# Python automatically closes the file.
#
# Therefore, using "with" is considered
# the best practice.


# ==========================================================
# Summary
# ==========================================================

# open()
# -------
# Opens a file.
#
# read()
# -------
# Reads the entire file.
#
# readline()
# -----------
# Reads one line.
#
# readlines()
# ------------
# Reads all lines into a list.
#
# write()
# --------
# Writes data to a file.
#
# append ("a")
# ------------
# Adds new data without deleting old data.
#
# write ("w")
# -----------
# Deletes old data and writes new data.
#
# close()
# --------
# Closes the file.
#
# with open()
# -----------
# Recommended way to work with files because
# it automatically closes the file.
#
# ==========================================================
