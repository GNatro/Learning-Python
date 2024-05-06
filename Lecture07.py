# This is the most exciting lecture: The Lecture of Conditions

# IF Condition
x = 31

# So if the condition is true, the code within the IF block will execute. 
# Otherwise, the code outside of the IF block will be executed. 
if (x < 30):
    print(f"{x} is less than 30")  # f-string to format the output

print("Out of the if condition")  # This will always print because it's outside the IF block

# IF/ELSE

x = 31

# If the condition is true, the code within the IF block will execute. 
# Otherwise, the code within the ELSE block will be executed.
if (x < 30):
    print(f"{x} is less than 30")
else:
    print(f"{x} is more than 30")  # f-string to format the output

# IF/ELIF/ELSE

x = 41

# This checks if x is less than 41. 
# If true, the code within the IF block executes.
if (x < 41):
    print(f"{x} is less than 41")

# This checks if x is equal to 41 (elif stands for else if). 
# If the previous condition (x < 41) was False and this condition is True, 
# the code within this block executes. 
elif x == 41:
    print("Equals to 41")

# If none of the above conditions are True, the ELSE block executes.
else:
    print(f"{x} is more than 41") 
