my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:] #taking indexless slice of my_foods createws a copy instead of passing reference

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
    print(food)

print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(food)
