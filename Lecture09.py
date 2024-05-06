# For Loop

# Looping through characters in a string (Technically not slicing)
PLANET = "Earth"
for i in PLANET:  # The loop iterates over each character in PLANET
    print("Value of i is now:", i)  # This will print each character
print("Rest of the code.")

# Looping through elements in a tuple
VACCINES = ("Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca")

for vac in VACCINES:  # The loop iterates over each vaccine name in VACCINES
    print(f"{vac} vaccine provides Immunization against covid19")

# Looping through elements in a list (similar to tuple loop)
VACCINES = ["Moderna", "Pfizer", "Sputnik v", "Covaxin", "AstraZeneca"]

for vac in VACCINES:  # The loop iterates over each vaccine name in VACCINES
    print(f"{vac} vaccine provides Immunization against covid19")


# While Loop (already explained)

x = 0
while x <= 10:  # This condition keeps the loop running as long as x is less than or equal to 10
    print("Value of X is:", x)
    print("Looping")
    x += 1  # Increment x by 1 after each iteration

print("Rest of the code.")
