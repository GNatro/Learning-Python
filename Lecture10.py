#This Lecture is a continuation of the previous Lecture 9. In this case we are making an overview of the Nested Loop

import time #We are importing a time module to use the sleep function.

# Here's a list of some vaccines
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]

# Let's loop through VACCINES
for vac in VACCINES:
  print("")  # Add an empty line for spacing
  print("Hey there, I'm thinking...")  # Simulate a thought process
  time.sleep(1)  # Pause for a dramatic effect (1 second)
  print("I would like to take a shot of...")
  # Now, let's spell out the name of the vaccine slowly (one letter at a time)
  for i in vac:
    print(i, end=" ")  # Print each letter with a space, not a new line
  print("\n")  # Add a new line after printing the whole vaccine name
  time.sleep(1)  # Another pause for suspense
"""
# This is an infinite loop (be careful!)
x = 2
while True:
  print("The value of X is now:", x)
  print("Whoa, X is getting bigger! Let's loop again...")
  x *= 2  # Double the value of X in each iteration
  time.sleep(1)  # Wait for 1 second before looping again

# **Important note:** This infinite loop will keep running until you manually stop the program. 
# Be sure to use `Ctrl+C` (or `Command+C` on macOS) to interrupt it when you're done.
"""