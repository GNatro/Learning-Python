# Variable Assignments
# We've seen variable assignments before, but let's go over them in more detail.

# There are different types of variables
var1 = "Python"  # This is a string
var2 = 75       # This is an integer
var3 = 3.5       # This is a float
var4 = True      # Boolean variable
var5 = False      # Boolean variable

"""Python is an intelligent programming language. You don't need to specify the variable 
type like in C++. However, this can make Python slower for specific tasks."""

# Printing Variables
print(var1)
print(var2)
print(var3)
print(var4)
print(var5)

# Check variable type
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
print(type(var5))

# Multiple Assignments
a = b = c = 65
"""This means c is assigned the value of b, which is assigned the value of a. So printing 
any of these variables will result in 65."""

print(a)
print(b)
print(c)

# Multiple Values Assigned to Multiple Variables
x, y, z = "alpha", "beta", 12

print(x, y, z)  # Print multiple variables at once

print("Variable x value is:", x)  # Print text with a variable inside

# Lists
first_list = [var1, "DevOps", 47, var2, 1.5]  # Lists can store various data types

print(first_list)  # Printing the entire list shows all stored data

print(first_list[0])  # Access specific data using its index (0 for the first element)

"""To access specific data in a list, use its numerical index. Remember, indexing starts
 from 0, not 1. You can manipulate lists by adding, editing, or removing items. Explore list
 manipulation further."""

# Tuples
first_tuple = (var1, "DevOps", 47, var2, 1.5)

print(first_tuple)

"""Tuples are similar to lists, but their data is read-only. You cannot add, edit, or 
remove items from a tuple."""

# Dictionaries
first_dictionary = {"Name": "George", "Weight": 75, "Exercises": ["Kickboxing", "Dancing", "Swimming"]}

"""Dictionaries store key-value pairs. You can store various data types, including lists, 
tuples, and other dictionaries. Dictionaries allow data manipulation (adding, removing, or
 editing). Explore dictionary manipulation in detail."""

print(first_dictionary)  # Print the entire dictionary

print(first_dictionary["Exercises"])  # Access data using its key
