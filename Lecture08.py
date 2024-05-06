"""
This script will implement our knowledge on
conditions and different datatypes.
"""

# Print a welcome message
print("This IT Organization has various skill sets.")
print("Find out your match.")

# Ask the user to enter their desired skill in capitalized letters
print("Enter Capitalised Values: ")

# Define some lists and dictionaries to store skill information
DevOps = ["Jenkins", "Ansible", "Bash", "Python", "Puppet", "Dockers", "Kubernetes", "Terraform"]
Development = ("Nodejs", "Angularjs", "Java", ".net", "Python")
cntr_emp1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 1024}
cntr_emp2 = {"Name": "Rocky", "Skill": "AI", "Code": 1218}

# Get the user's desired skill as input
usr_skill = input("Enter your desired skill: ")

# Check if the user's skill is in the DevOps list
if usr_skill in DevOps:
    print(f"We Have {usr_skill} in DevOps Team.")
# Check if the user's skill is in the Development tuple
elif (usr_skill in Development):
    print(f"We have {usr_skill} in Development Team.")
# Check if the user's skill matches any skill of the contract employees (in their skill value)
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print(f"We have contract employees with {usr_skill} skill.")
# If none of the above conditions are met, the skill is not found
else:
    print("Skill not found")
    print("Please check if you have entered value in capitalize or check the spelling.")
