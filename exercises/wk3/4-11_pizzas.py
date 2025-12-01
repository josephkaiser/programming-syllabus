# 4-1 program
pizzas = ["caprese", "margarita", "pepperoni"]
for pizza in pizzas:
    print(f"i like {pizza}\n")

print(f"I really like all these pizzas!")

# new 4-11 addition
friend_pizzas = pizzas[:]  # make a copy

pizzas.append("hawaiian")

friend_pizzas.append("chicken nugget")

print(f"my favorite pizzas:")
for pizza in pizzas:
    print(pizza)

print(f"friend's favorite pizzas:")
for pizza in friend_pizzas:
    print(pizza)
