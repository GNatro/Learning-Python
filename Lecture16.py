# Variable Length Arguments *args (Non keyword Arguments)

def order_food(min_order, *args):
  """
  This function takes a minimum order requirement and any number of additional food items as arguments.

  Args:
      min_order (str): The minimum order requirement.
      *args: Variable length arguments representing additional food items (non-keyword arguments).
  """
  print(f"You have ordered: {min_order}")
  # Print the additional food items using a loop
  for item in args:
    print(f"You have ordered: {item}")
  print("Your food will be delivered in 30 mins:")
  print("Enjoy the party")

order_food("Salad", "Pizza", "Biryani", "Soup")

"""*args: This syntax allows the function to accept a variable number of arguments. These arguments are packed into 
a tuple named args inside the function.

In the order_food function definition, min_order is a regular argument, while *args captures any additional arguments
 passed to the function.

When you call order_food("Salad", "Pizza", "Biryani", "Soup"), all the arguments after min_order ("Salad", "Pizza", 
"Biryani", "Soup") are collected as a tuple within args.

The for loop iterates through the args tuple, printing each additional food item.
Using *args provides flexibility when you don't know beforehand how many additional arguments a function might 
receive."""
