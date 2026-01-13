user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# items() to iterate over key and value
for k, v in user_0.items():
    print(f"\nKey: {k}\nValue: {v}\n")

# keys() to iterate over keys only
for k in user_0.keys():
    print(k.title())

# rely on default behavior of dictionary to iterate over keys
for k in user_0:
    print(k.title())

# Try iterate over values
for v in user_0.values():
    print(v.title())
