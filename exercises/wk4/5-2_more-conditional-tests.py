# 5-2. More Conditional Tests: You don’t have to limit the number of tests you
# create to 10. If you want to try more comparisons, write more tests and add
# them to conditional_tests.py. Have at least one True and one False result for
# each of the following:
# •Tests for equality and inequality with strings
# •Tests using the lower() function
# •Numerical tests involving equality and inequality, greater than and
# less than, greater than or equal to, and less than or equal to
# •Tests using the and keyword and the or keyword
# •Test whether an item is in a list
# •Test whether an item is not in a list

# Equality & inequality with strings
string1 = "string"
string2 = "string"
print(string1 == string2)                       # True
print(string1 != string2)                       # False

# Using lower() function
string1 = "STRING"
string2 = "string"
print(string1 == string2)                       # False
print(string1.lower() == string2.lower())       # True

# Numerical tests involving equality/inequality, greater and less than, greater than or equal to and less than or equal to
zero = 0
one = 1
print(zero != one)                              # True
print(zero == one)                              # False
print(zero > one)                               # False
print(zero < one)                               # True
print(zero >= one)                              # False
print(zero <= one)                              # True

# Test using and / or logical operators
print(zero != one or zero == one)               # True
print(zero != one and zero == one)              # False
print(string1 == string2 and zero != one)       # False

# Test in / not in
strings = [string1, string2]
numbers = [zero, one]

print(string1 in strings and zero in numbers)   # True
print(string1 in numbers or one in numbers)     # True
print(string2 not in numbers)                   # True
print(one in numbers)                           # True
