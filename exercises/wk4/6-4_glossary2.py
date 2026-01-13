'''
6-4_glossary2.py
PCC
Chapter 6
Ex. 4
'''

glossary = {
    'dictionary': 'a data structure that represents key-value pairs.',
    'key': 'the first item in the key-value pair, which is the reference label.',
    'value': 'the second item in the key-value air, which is the value attributed to the label.',
    'if-elif-else chain': 'a flow control structure used to check and handle conditions in sequence.',
    'del': 'a statement to delete any item following it.',
    'object': 'a basic kind in programming. Can be of various types and data.',
    'for': 'looping command to repeat block of code set number of times.',
    'while': 'looping command to repeat block of code until condition.',
    'program': 'a file containing code to be run.'
}

for word, definition in glossary.items():
    word_print = word.title()
    definition_print = '. '.join(i.capitalize() for i in definition.split('. ')) # Handle sentence case
    print(f"{word_print}:\n\t{definition_print}")
