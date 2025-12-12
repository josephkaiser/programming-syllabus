'''
toppings.py
Python Crash Course
Chapter 5
'''

available_toppings = ['mushrooms', 'extra cheese', 'green peppers', 
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'extra cheese', 'green peppers', 'pineapple', 'bacon']

# requested_toppings = [] # Makes empty list

if requested_toppings: # Checks that list is not empty
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings: # Compare each item in list A vs. list B
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
    print("\nFinished making your pizza!")
else: # If list is empty
    print("Are you sure you want a plain pizza?")
