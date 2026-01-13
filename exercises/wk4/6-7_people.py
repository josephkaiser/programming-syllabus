john_data = {
    'first_name': 'john',
    'last_name': 'henry',
    'age': 20,
    'city': 'portland'
}

susan_data = {
    'first_name': 'susan',
    'last_name': 'morgan',
    'age': 65,
    'city': 'tacoma'
}

jimmy_data = {
    'first_name': 'jimmy',
    'last_name': 'burgess',
    'age': 32,
    'city': 'houston'
}

people = [john_data, susan_data, jimmy_data]

for person in people:
    full_name = person['first_name'].title() + " " + person['last_name'].title()
    print("\n"
        + full_name
        + " lives in "
        + person['city'].title()
        + " and is "
        + str(person['age'])
        + " years old.")
