# cars = []
# car_input = ''
# while car_input != 'q':
#     car_input = input('Enter a car type: ').lower()
#     if car_input == 'q':
#         break
#     cars.append(car_input)
# car_matrix = [cars[:] for _ in range(len(cars))]
# print(car_matrix)
# models = ['coupe', 'hatchback', 'convertible', 'roadster']

cars = ['bmw', 'audi', 'nissan', 'subaru', 'porsche']

print('given order', '\t\t\t', cars)
cars.reverse()
print('reverse order', '\t\t\t', cars)

# Method 1: sort(obj)
print('abc order', '\t\t\t', sorted(cars))

# Method 2: obj.sort()
cars.sort()
print('abc order', '\t\t\t', cars)

cars.sort(reverse=True)
print('reverse abc order', '\t\t', cars)
