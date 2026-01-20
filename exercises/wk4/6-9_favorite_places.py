favorite_places = {
    'joe': ['los angeles', 'san francisco', 'chicago'],
    'maya': ['los angeles', 'new york', 'paris'],
    'john': ['los angeles', 'chicago', 'new york']
}

for person, places in favorite_places.items():
    print("\n" + person.title() + "'s favorite places are:")
    for place in places:
        print("\t" + place.title())
