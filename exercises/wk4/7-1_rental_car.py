prompt = "What kind of rental car would you like? \n"
user_input = input(prompt)
cars = ['subaru', 'toyota', 'porsche', 'ford', 'audi', 'bmw']
if user_input.lower().strip() in cars:
    print("\nYes, we have a " + user_input + " in our collection.")
else:
    print("\nSorry, we do not have a " + user_input + " in our collection. Please choose from the following models: ")
    for car in cars:
        print(car)
