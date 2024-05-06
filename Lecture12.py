#Continuation of BREAK and CONTINUE

#We are gonna add a random module

import random

VACCINES = ["Moderna", "Pfizer", "Sputnik", "Covaxin", "AstraZeneca", "CoronaVac"]

random.shuffle(VACCINES)
print(VACCINES)


# The difference betwen choice and shuffle is that choice only chooses one of list 
LUCKY = random.choice(VACCINES)
print(LUCKY)

"""
for vac in VACCINES:
    print(f"*******TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("#################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("#################")
        print() 
        break #So When it matches LUCKY with vac it will output successful and will exit
    print("XXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXX")
    print()
"""


for vac in VACCINES:
    print(f"*******TESTING VACCINE {vac}")
    if vac == LUCKY:
        print("#################")
        print(f"{LUCKY} Vaccine, Test SUCCESSFUL")
        print("#################")
        print() 
        continue #So When it matches LUCKY with vac it will output successful and will continue until the finish
    print("XXXXXXXXXXXXXX")
    print("Test Failed")
    print("XXXXXXXXXXXXXX")
    print()