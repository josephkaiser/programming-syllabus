fluffy = {
    'name': 'fluffy',
    'animal': 'dog',
    'owner': 'hagrid',
}

jolene = {
    'name': 'jolene',
    'animal': 'dog',
    'owner': 'jesse',
}

sassy = {
    'name': 'sassy',
    'animal': 'cat',
    'owner': 'susan',
}

pets = [fluffy, jolene, sassy]

for pet in pets:
    print("\n"
        + pet['name'].title()
        + " is a "
        + pet['animal']
        + " owned by "
        + pet['owner'].title())
