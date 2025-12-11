'''
Amusement Park tiered pricing example

Admission for anyone under age 4 is free
Admission for anyone 4 - 18 is $5
Admission for anyone 18+ is $10
Admission for seniors 65+ is $5
'''

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65: # Use final elif block and omit else block for confidence that code will only run under correct conditions
    price = 5

print(f"Your admission cost is ${price:.2f}.")
