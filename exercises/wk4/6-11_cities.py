cities = {
    'los angeles': {
        'country': 'The United States of America',
        'population': 13000000,
        'fact': 'The full original name of Los Angeles is "El Pueblo de Nuestra Señora la Reina de los Ángeles de Porciúncula," which translates to "The Town of Our Lady the Queen of Angels of Porciúncula." This name reflects the citys Spanish colonial roots.'
    },

    'san francisco': {
        'country': 'The United States of America',
        'population': 827526,
        'fact': 'San Francisco is known for its iconic Golden Gate Bridge, which was originally proposed to be painted black and yellow before settling on its now-famous International Orange color. The city is also home to the largest and oldest Japantown in the United States.'
    },

    'new york': {
        'country': 'The United States of America',
        'population': 8800000,
        'fact': 'New York City is the most populous city in the United States, with over 8 million residents, and is known for its linguistic diversity, with over 800 languages spoken.'
    },
}

for city in cities.keys():
    print(f"\n{city.title()}:")
    for attribute, value in cities[city].items():
        if attribute == 'country':
            print(f"\tLocated within {value}.")
        elif attribute == 'population':
            print(f"\tHome to approximately {value:,} people.")
        else:
            print(f"\tFun fact: {value}")
