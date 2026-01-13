'''
favorite_languages.py
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    '_zir': 'c',
    '1zir': 'c++',
}

print("\nLooping through all key-value pairs in dictionary")

'''Looping through all key-value pairs in dictionary'''
for name, language in sorted(favorite_languages.items()):
    print(name.title()
        + "'s favorite language is "
        + language.title()
        + ".")

print("\nLooping through the keys of dictionary")

'''Looping through the keys of dictionary'''
for name in sorted(favorite_languages.keys()):
    print(name.title()
        + "'s favorite language is "
        + favorite_languages[name].title()
        + ".")

print("\nfriends & erin")

'''friends & erin'''
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(f"\tHi {name.title()}, I see your favorite language is {favorite_languages[name].title()}!")

print("\n")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n")

'''Looping through values in a dictionary'''
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):   # Unique values via set
    print(language.title())

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
