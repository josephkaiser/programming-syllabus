pets = {
    'fluffy': {
        'name': 'fluffy',
        'animal': 'dog',
        'owner': 'hagrid',
    },
    
    'jolene': {
        'name': 'jolene',
        'animal': 'dog',
        'owner': 'jesse',
    },
    
    'sassy': {
        'name': 'sassy',
        'animal': 'cat',
        'owner': 'susan',
    },
}




for pet_name, pet_info in pets.items():
    print(f"{pet_name.title()} is a "
        + pet_info['animal'] + " owned by "
        + pet_info['owner'].title() + ".")
