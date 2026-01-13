'''
6-2_favorite_number.py
PCC
Chapter 6
Ex. 2
'''

favorite_numbers = {
    'spongebob': 25,
    'elon': 420,
    'fat albert': 3.14159,
    'euler': 2.71,
    'newton': 9.81,
    'gen z': 67,
}

for name, number in favorite_numbers.items():
    print(f"{number}\t is {name.title()}'s favorite number.")
