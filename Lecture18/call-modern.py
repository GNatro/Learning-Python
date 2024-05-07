# Importing the 'modern' module

import modern

# This line is commented out as it's not used in the subsequent code. 
# uncomment it if you want to see all the attributes and functions available in the 'modern' module.
#print(dir(modern)) 

# Calling functions from the 'modern' module

# order_food function with variable length arguments (*args)
modern.order_food("Salad", "Pizza", "Biryani", "Soup")  # Calling with positional arguments

"""
This line calls the order_food function from the 'modern' module.
The order_food function likely takes a minimum order requirement as the first argument 
and any number of additional food items as separate arguments.
"""

# vac_feedback function with keyword arguments (**kwargs)
modern.vac_feedback(efficacy=34, vac="Unknown")  # Calling with keyword arguments

"""
This line calls the vac_feedback function from the 'modern' module.
The vac_feedback function likely takes arguments related to a vaccine, 
where 'vac' specifies the vaccine name (keyword argument) and 'efficacy' specifies 
the vaccine's efficacy percentage (keyword argument).
"""

# time_activity function with variable length arguments (*args, **kwargs)
modern.time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")

"""
This line calls the time_activity function from the 'modern' module.
The time_activity function likely takes a variable number of arguments representing 
minutes spent on activities (positional arguments) and any number of keyword arguments 
representing activities with their corresponding time spent (key-value pairs).
"""
