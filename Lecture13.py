# String Built-in Methods/Functions

message = "corona vaccine is ready to use, most of them are more than 90 percent effective."


print(message)

# Capitalize the first letter of the message (method)
print(message.capitalize())  # This creates a new string, doesn't modify the original

# Create a new variable Message with the capitalized version (assignment)
Message = message.capitalize()
print(Message)

#  --- Understanding dir() function ---

# Use dir() to explore built-in methods/attributes available for an empty string
print(dir(""))

# Explore methods/attributes for an empty list
print(dir([]))

# Explore methods/attributes for an empty tuple
print(dir(()))

# Explore methods/attributes for an empty dictionary
print(dir({}))

# --- String Built-in Methods Continued ---

# Convert message to all uppercase (method)
print(message.upper())

# Check if all characters in message are lowercase (method)
print(message.islower())  # This will return False

# Check if all characters in message are uppercase (method)
print(message.isupper())  # This will return False

# Find the index of the first occurrence of "ready" (method)
print(message.find("ready"))  # This will return 18

# Extract a substring from message (slicing)
print(message[18:24])  # This will print "read"

# Find the index of the first occurrence of "not" (method)
print(message.find("not"))  # This will return -1 because "not" is not found

# --- Working with Tuples and Strings ---

# Create a tuple named seq1 containing strings
seq1 = ("192", "168", "40", "90")

# Join the elements of seq1 with "." using join() method (built-in function on string)
print(".".join(seq1))  # This will print "192.168.40.90"

# Similar join using "/" as separator
print("/".join(seq1))  # This will print "192/168/40/90"

# Similar join using "-" as separator
print("-".join(seq1))  # This will print "192-168-40-90"

# --- Working with Lists ---

# Create a list named mountains containing mountain names
mountains = ["Everest", "Himalaya", "Sahyadri", "Alps", "K2", "Mt Hood"]

# Print the contents of the mountains list
print(mountains)  # This will print ["Everest", "Himalaya", ...]

# Append a new element ("Oregon mount") to the end of the list (method)
mountains.append("Oregon mount")
print(mountains)  # This will print ["Everest", "Himalaya", ..., "Oregon mount"]

# Extend the list mountains by adding elements from another list (method)
mountains.extend(["Mt Rainer", "Satpuda"])
print(mountains)  # This will print all mountains including "Mt Rainer" and "Satpuda"

# Insert an element ("Mt Abu") at a specific index (2) in the list (method)
mountains.insert(2, "Mt Abu")
print(mountains)  # This will print the list with "Mt Abu" inserted at index 2

# Remove and return the last element from the list (method)
mountains.pop()
print(mountains)  # This will print a shorter list after removals

# Remove the element at index 5 from the list (method)
mountains.pop(5)
print(mountains)  # This will print the final list with the element at index 5 removed

# --- Working with Dictionaries ---

# Create a dictionary named cntr_emp1 to store employee information (key-value pairs)
cntr_emp1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 1024}

# Get a view of the dictionary's keys (method)
print(cntr_emp1.keys())  # This will print a dictionary view of the keys

# Get a view of the dictionary's values (method)
print(cntr_emp1.values())  # This will print a dictionary view of the values

# Clear all key-value pairs from the dictionary (method)


#Here is an explanation from Gemini AI about Functions, Built-in Functions, Modules and Atributes, just to clarify a little bit:

"""
Here's a breakdown to differentiate between functions, methods, built-in functions, attributes, and modules:

Functions:

Definition: Independent blocks of code that can be defined anywhere in your program. They perform specific tasks and can be reused throughout your code.
Calling: Functions are called directly using their name followed by parentheses (optionally containing arguments).
Scope: Functions have their own local scope, meaning variables defined within a function are not accessible outside of it unless explicitly returned or made 
global (generally not recommended).
Examples: print(), len(), or user-defined functions you create from scratch.
Methods:

Definition: Functions that are associated with a specific object. They are defined within a class and operate on data (attributes) of that object.
Calling: Methods are called using dot notation (.) on an object instance followed by the method name and parentheses (optionally containing arguments).
Scope: Methods can access the object's attributes directly, and they might also have their own local scope for variables defined within the method.
Examples: Methods defined within classes to perform actions specific to those objects (e.g., list.append(), object.toString()).
Analogy:

Think of functions as general-purpose tools available to your entire program.
Think of methods as specialized tools designed to work on specific objects.
Built-in Functions:

Availability: Built-in functions are available by default in the Python interpreter, so you don't need to import any module to use them.
Examples: len(), print(), int(), str(), range(), etc.
Use Case: Common functionality for various programming tasks.

Modules:

Definition: Python files containing functions, classes, and variables that you can import and use in your program.
Importing: You need to use the import statement to make the functionalities from a module available in your code.
Examples: math, os, random, etc. (These modules provide functionalities related to math operations, operating system interactions, random number 
generation, etc.)
Use Case: Provide specialized functionalities for specific domains or tasks that are not built-in to the Python interpreter.

Attributes:

Definition: Variables that store data associated with an object or module.
Examples: In a list, each element is an attribute. In a dictionary, each key-value pair is an attribute. In a class instance, the variables 
that define the object's state are its attributes.

In simpler terms:

Functions are like tools in your toolbox, ready to be used whenever you need them.
Methods are like specialized tools designed for specific objects in your toolbox.
Built-in functions are like pre-installed tools that come with the Python interpreter.
Modules are like additional toolsets you can import to expand your capabilities.
Attributes are like labels on the tools (or data stored within them) that tell you what they are and what they can do.

"""