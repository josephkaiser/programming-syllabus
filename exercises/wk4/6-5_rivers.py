'''
Dictionary containing three major rivers & country each river runs through
'''

rivers = {
    'nile': 'egypt',
    'mississippi': 'usa',
    'seine': 'france',
    'thames': 'britain',
    'danube': 'germany'
}

'''Use a for loop to print sentence about each river'''
for river, country in rivers.items():
    river_print = river.title()
    country_print = 'the ' + country.upper() if country == 'usa' else country.title()
    print(f"The {river_print} runs through {country_print}.")

'''Use a loop to print name of each river in dictionary'''
print(f"\nUse a loop to print name of each river in dictionary")
for river in rivers.keys():
    print(river.title())

'''Use a loop to print the name of each country in dictionary'''
print(f"\nUse a loop to print the name of each country in dictionary")
for country in rivers.values():
    country_print = country.upper() if country == 'usa' else country.title()
    print(country_print)
