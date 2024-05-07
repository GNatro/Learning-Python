# Variable Length Arguments **kwargs (keyword Arguments)

import random


def time_activity(*args, **kwargs):
  """
  This function takes a variable number of minutes as positional arguments 
  and any number of key-value pairs representing activities as keyword arguments.

  Args:
      *args: Variable length arguments representing minutes spent on activities (non-keyword arguments).
      **kwargs: Keyword arguments representing activities (key=value pairs).

  Returns:
      A string indicating the total recommended time and a randomly chosen activity.
  """
  # Sum the minutes from positional arguments
  min = sum(args)

  # Add a random number of minutes (0 to 60)
  min += random.randint(0, 60)

  # Choose a random activity from the keyword arguments
  choice = random.choice(list(kwargs.keys()))

  # Return a formatted string with the total time and chosen activity
  return f"You have to spend {min} Minutes for {kwargs[choice]}"


# Example usage
result = time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")
print(result)


#Here is an explanation of Gemini AI:

"""Explanation of **kwargs:

**kwargs: This syntax allows the function to accept a variable number of keyword arguments. These arguments are 
packed into a dictionary named kwargs inside the function.
In the time_activity function definition, *args captures any positional arguments (minutes), while **kwargs captures 
any keyword arguments (activity names paired with time spent).
When you call time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps"), the positional 
arguments become a tuple in args and the keyword arguments become a dictionary in kwargs.
The random.choice(list(kwargs.keys())) part chooses a random key from the kwargs dictionary (activity name), and
kwargs[choice] retrieves the corresponding value (time spent).

Difference between args and kwargs:

*args: Captures a variable number of positional arguments (arguments passed in the order they appear in the function
 definition). Useful when you don't know how many arguments a function might receive, but they should be in a specific
   order.
**kwargs: Captures a variable number of keyword arguments (arguments passed as key-value pairs). Useful when you want

 to handle arguments with names and don't care about the order they are provided.
In summary:

Use *args for multiple arguments without keywords, where the order matters.
Use **kwargs for multiple arguments with keywords (key-value pairs), where the order doesn't matter."""