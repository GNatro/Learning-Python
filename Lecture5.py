# Slicing

planet1 = "Closest to the Sun"  

print(planet1)

print(planet1[0])
print(planet1[1])
print(planet1[2])

# Negative index slicing

print(planet1[-1])
print(planet1[-2])
print(planet1[-3])

# Slicing a string, get a substring from a string

print(planet1[1:4])  # Extract characters from index 1 (inclusive) to 4 (exclusive)

print(planet1[:7])  # By default, it starts from the 0 position (up to index 7, exclusive)

# Slicing a tuple

devops = ("Linux", "Vagrant", "Bash Scripting", "AWS", "Jenkins", "python", "Ansible")

print(devops[2])  # We are accessing the element "Bash Scripting" at index 2 and outputting it

print(devops[2][5:11])  # Extract a substring from "Bash Scripting": "Script" (from index 5 to 11, exclusive)

print(devops[2][5:14][-1])  # Extract a substring, then get the last character ('g') using negative slicing

"""
We can do the same with Dictionaries, accessing the data is simple once you know the rules 
we have covered previously. But I won't waste time explaining this, because it's almost the same.
"""
