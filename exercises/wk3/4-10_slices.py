cubes = [value**3 for value in range(1, 11)]
print(*cubes, sep="\n")

print(f"the first three items in the list are: {cubes[0:3]}")

print(f"three items from the middle of the list are: {cubes[4:7]}")

print(f"the last three items in the list are: {cubes[-3:]}")
