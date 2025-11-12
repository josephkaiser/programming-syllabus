age = input('input age: ')
age_str = str(age)
n = len(age_str) - 1
if age_str[n] == '1':
    ordinal = "st"
elif age_str[n] == '2':
    ordinal = "nd"
elif age_str[n] == '3':
    ordinal = "rd"
else:
    ordinal = "th"

message = "Happy " + str(age) + ordinal + " Brithday!"
print(message)
