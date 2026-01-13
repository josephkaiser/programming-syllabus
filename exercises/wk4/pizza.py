# New function to summarize the order.
def print_order(pizza):
    print("You ordered a "
            + pizza['crust']
            + "-crust pizza "
            + "with the following toppings:")
    for topping in pizza['toppings']:
        print("\t" + topping)

# List as a dictionary value.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# Call function to summarize order.
print_order(pizza)

# Change the order.
pizza['crust'] = 'thin'
pizza['toppings'] = ['cheese', 'tomato', 'mozzarella']

# Call function to summarize order.
print_order(pizza)
