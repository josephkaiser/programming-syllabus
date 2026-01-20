print("Welcome to the movies!")

prompt = "\nWhat is your age? "
while True:
    age = input(prompt)
    try:
        age = int(age)
    except TypeError as e:
        raise e

    if age < 3:
        price = 0
    elif (3 <= age) & (age < 12):
        price = 10
    elif (12 <= age):
        price = 15

    print(f"The ticket price for you would be ${price:,}.00")
