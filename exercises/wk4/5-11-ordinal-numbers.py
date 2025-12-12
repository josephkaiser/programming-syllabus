'''
5-11-ordinal-numbers.py
correctly assign st, nd, rd, th endings to numbers
'''

numbers = list(range(1,10)) # List of integer numbers from 1 to 9

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    elif 2 < number <= 9:
        print(f"{number}th")

# Try for larger numbers

numbers = list(range(1,100))

for number in numbers:
    last_numeral = int(str(number)[-1])
    if last_numeral == 1:
        print(f"{number}st")
    elif last_numeral == 2:
        print(f"{number}nd")
    elif last_numeral == 3:
        print(f"{number}rd")
    elif 2 < last_numeral <= 9:
        print(f"{number}th")
