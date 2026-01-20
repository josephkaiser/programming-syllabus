# Remove all instances of specific values from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', 'cat']

counter = 0
while 'cat' in pets:
    pets.remove('cat')
    counter += 1

print(pets)
print(str(counter) + " instances of 'cat' removed.")
