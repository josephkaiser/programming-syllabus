requested_toppings = ['mushrooms', 'extra cheese', 'green peppers']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese")


# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

requested_toppings = [] # Makes empty list

if requested_toppings: # Checks that list is not empty
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else: # If list is empty
    print("Are you sure you want a plain pizza?")
