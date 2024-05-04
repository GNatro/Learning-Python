# In this lecture, we will see the ways we can use the `print` function
# to display many things.

name = "sars_cov_2"
disease = "Covid19"

# Print using string formatting (older method)
print("The name of the virus is:", name)
print("The name of the virus is {}".format(name))
print("{} is the name of the virus.".format(name))

# Print using f-strings (formatted string literals - newer method)
print(f"The name of the virus is {name} and it causes {disease}")

# Print using concatenation (less preferred for longer strings)
print("The name of the virus is " + name)
