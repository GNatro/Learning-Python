# Building our own Functions

# Defining Functions

def add(arg1, arg2):
  """
  This function adds two numbers and returns the sum.

  Args:
      arg1: The first number.
      arg2: The second number.

  Returns:
      The sum of arg1 and arg2.
  """
  total = arg1 + arg2
  return total

out = add(2, 3)

print(out)
print(add(10, 30))


def summ(arg):
  """
  This function calculates the sum of elements in a list.

  Args:
      arg: A list of numbers.

  Returns:
      The sum of the elements in the list.
  """
  x = 0
  for i in arg:
    x = x + i
  return x


out = summ([10, 20, 30])
print(out)

# This line will cause an error because summ can only take one list as input
# summ([10,20],[30,50])


# Default Argument
def greetings(MSG="Morning"):
  """
  This function prints a greeting message with a default value for MSG.

  Args:
      MSG: The greeting message (default is "Morning").
  """
  print(f"Good {MSG}")
  print("Welcome to the function.")


greetings()
greetings("Evening")
