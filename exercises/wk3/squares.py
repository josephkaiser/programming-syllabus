# Method 1: Using variable assignment
squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# Method 2: Using expression in argument of function
squares = []
for value in range(1,11):
    squares.append(value**2)

print(squares)

# Method 3: Using list comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
