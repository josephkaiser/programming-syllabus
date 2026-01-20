print("Welcome to Joe's Pizza Shoppe!")

toppings = ['cheese', 'tomato sauce']
prompt = "\nWhat toppings would you like on your pie? "
active = True

while active:
    topping = input(prompt).lower().strip()
    if topping == 'quit':
        active = False
    elif topping not in toppings:
        print(f"Yes, we will add {topping} to the pizza.")
        toppings.append(topping)
    else:
        print(f"Yes, we already have {topping} being added to the pie.")
    prompt = "\nGot it. Anything else? (or enter 'quit') "

print("Your pizza pie is ready with following toppings:")
for topping in toppings:
    print(topping)
