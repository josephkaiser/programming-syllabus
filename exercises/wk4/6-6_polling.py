'''
6-6_polling.py
PCC
Ch 6
Ex 6

Use the code in favorite_languages.py pg 104
    - make a list of people who should take the poll. Include names already in dictionary and new names
    - Loop throuhg the list of people who should take the poll. If they have already taken the poll, print a message thanking them for responding. If not, print a  message inviting them to take the poll
'''

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

pollees = {
    'john',
    'jen',
    'sarah',
    'joe'
}

for pollee in pollees:
    print(f"\n{pollee}: ")
    if pollee in favorite_languages.keys():
        print("\tThank you for taking the poll!")
    elif pollee not in favorite_languages.keys():
        print("\tWe invite you to take the poll.")
