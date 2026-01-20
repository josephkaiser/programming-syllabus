print("Welcome to the movies!")

prompt = "\nWhat is your age? "
count = 0
subtotal = 0
active = True
while active:
    age = input(prompt)

    if age == 'quit':
        break

    try:
        age = float(age)
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
    subtotal += price
    count += 1
    if count >= 5:
        print(f"Sorry, the limit is {count} tickets per group.")
        active = False

tax = 0.091 * subtotal

total = tax + subtotal

print(f"Your total comes to ${total:,.2f}, subtotal of ${subtotal:,.2f} and tax of ${tax:,.2f}")
