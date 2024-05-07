# Keyword arguments

def vac_feedback(vac, efficacy):
  """
  This function provides feedback on a vaccine based on its efficacy.

  Args:
      vac (str): The name of the vaccine.
      efficacy (int): The efficacy of the vaccine (percentage).
  """
  print(f"{vac} Vaccine is having {efficacy} % efficacy.")
  if (efficacy > 50) and (efficacy <= 75):
    print("Seems not so effective, Needs more trial.")
  elif (efficacy > 75) and (efficacy < 90):
    print("Can consider this vaccine.")
  elif efficacy >= 90:
    print("Sure, will take the shot.")
  else:
    print("Needs many more trials.")

#vac_feedback("Pfizer", 95)  # Calling with positional arguments
#vac_feedback("Unknown", 45)

# Calling with keyword arguments (order doesn't matter)
vac_feedback(efficacy=34, vac="Unknown")
vac_feedback(vac="Covaxin", efficacy=80)


"""Keyword arguments: When calling a function, you can specify the values for arguments by name instead of their 
positional order. This makes the code more readable, especially when functions have many arguments.
In the vac_feedback function definition, vac and efficacy are defined as arguments.

In the function calls at the bottom, you can see two approaches:

Positional arguments: Here, you provide values in the same order as the arguments defined in the 
function (e.g., vac_feedback("Pfizer", 95)).

Keyword arguments: Here, you explicitly specify the argument names followed by their corresponding 
values (e.g., vac_feedback(efficacy=34, vac="Unknown")). The order in which you provide these keyword arguments
doesn't matter."""