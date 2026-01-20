prompt = "How many guests in your party? \n"
user_input = input(prompt)
guests_requested = int(user_input)
if guests_requested > 8:
    print("You'll need to wait for a table.")
else:
    print("Your table is ready. Please follow me.")
