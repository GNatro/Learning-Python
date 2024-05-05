# Operators


# What are the basic operators?

x = 2  # Assignment operator assigns the value 2 to variable x
y = 5  # Assignment operator assigns the value 5 to variable y

total = x + y  # Addition operator adds x and y
total1 = x - y  # Subtraction operator subtracts y from x
total2 = x * y  # Multiplication operator multiplies x and y
total3 = x / y  # Division operator divides x by y (returns a float)
total4 = x % y  # Modulo operator gives the remainder of x divided by y
total5 = y ** x  # Exponentiation operator raises y to the power of x

print(total)
print(total1)
print(total2)
print(total3)
print(total4)
print(total5)

# What are the comparison operators?

a = 30
b = 60

out = (a < b)  # Less than operator checks if a is less than b
print(out)

out = (a == b)  # Equal to operator checks if a is equal to b
print(out)

out = (a != b)  # Not equal to operator checks if a is not equal to b
print(out)

out = (a >= b)  # Greater than or equal to operator checks if a is greater than or equal to b
print(out)

out = (a <= b)  # Less than or equal to operator checks if a is less than or equal to b
print(out)

# Assignment Operators

c = 0
d = 1
c += d  # Augmented assignment operator (c = c + d) adds d to c
print(d)

c = 0
d = 1
c -= d  # Augmented assignment operator (c = c - d) subtracts d from c
print(c)

# Logical Operators

# and, or

a = 40
b = 60
x = 2
y = 3

out = (a < b) or (x > y)  # Or operator checks if at least one condition is True
print(out)

out = (a > b) or (x < y)  # Or operator checks if at least one condition is True
print(out)

out = (a > b) or (x > y)  # Or operator checks if at least one condition is True
print(out)

out = (a > b) and (x < y)  # And operator checks if both conditions are True
print(out)

out = (a < b) and (x < y)  # And operator checks if both conditions are True
print(out)

out = not(x < y)  # Not operator inverts the truth value of the condition
print(out)

# Membership Operator

first_tuple = ("IOT", "DevOps", 47, 89, 1.5)

ans = "DevOps" in first_tuple  # In operator checks if "DevOps" is present in first_tuple
print(ans)

ans = "DevOps" not in first_tuple  # Not in operator checks if "DevOps" is not present in first_tuple
print(ans)

ans = 67 in first_tuple  # In operator checks if 67 is present in first_tuple
print(ans)

# Identity Operators

a = 12
b = 15
result = a is b  # Is operator checks if a and b refer to the same object
print(result)

result = a is not b  # Is not operator checks if a and b do not refer to the same object
print(result)
