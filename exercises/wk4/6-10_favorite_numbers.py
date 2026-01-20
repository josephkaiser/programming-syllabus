favorite_numbers = {
    'spongebob': [25],
    'elon': [69, 420],
    'fat albert': [3.14159],
    'euler': [2.71],
    'newton': [9.81, 6.67],
    'gen z': [6, 7, 67],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in list(numbers):
        print(f"{number}")
