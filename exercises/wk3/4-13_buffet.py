foods = ("chicken", "brocoli", "tomato", "bread", "olive oil")
for food in foods:
    print(food)

try:
    foods[0] = "meatballs"
except TypeError as e:
    print(e)

foods = ("meatballs", "cauliflower", "tomato", "bread", "olive oil")
for food in foods:
    print(food)
