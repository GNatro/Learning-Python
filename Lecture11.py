#Break and Continue

#Break
# We are gona iterate with for loop in DevOps and if the i equals to O we are gonna print and break, so break means
# that we are gonna exit from that portion of code. 
"""

for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data.")
        break # Here we are exiting after i equals to O 
print("Out of Loop")"""

#Continue
for i in "DevOps":
    if i == "O":
        continue  # Here we are continuing after i equals to O, so it's basically skipping this part of code to 
        print("Found my data.") 
    print(f"Value of i is {i}")
print("Out of Loop")