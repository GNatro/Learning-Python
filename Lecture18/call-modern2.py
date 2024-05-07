# Importing all functions from the 'modern' module

from modern import *  # Importing all functions and variables from the 'modern' module

# Calling functions from the imported 'modern' module

order_food("Pizza")

"""
This line calls the order_food function directly without the 'modern.' prefix 
because all functions from 'modern' are imported using '*'.
The order_food function likely takes a minimum order requirement as the first argument.
"""

vac_feedback(efficacy=34, vac="Unknown")

"""
This line calls the vac_feedback function directly.
The vac_feedback function likely takes arguments related to a vaccine, 
where 'vac' specifies the vaccine name (keyword argument) and 'efficacy' specifies 
the vaccine's efficacy percentage (keyword argument).
"""

time_activity(10, 20, 10, hobby="Dance", sport="Boxing", fun="Driving", work="DevOps")

"""
This line calls the time_activity function directly.
The time_activity function likely takes a variable number of arguments representing 
minutes spent on activities (positional arguments) and any number of keyword arguments 
representing activities with their corresponding time spent (key-value pairs).
"""
