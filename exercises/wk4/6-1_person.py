'''
6-1_person.py
PCC
Chapter 6
Ex. 1
'''

user_data = {
    'first_name': 'john',
    'last_name': 'henry',
    'age': 20,
    'city': 'portland'
}

for key, value in user_data.items():
    print(f"{key.title()} is {value}")
