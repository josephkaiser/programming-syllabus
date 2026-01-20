prompt = "Please enter a number: "
user_input = input(prompt)
test_number = int(user_input)
if test_number % 10 == 0:
    multiple = int(test_number / 10)
    print("The number " + str(user_input) + " is 10 multiplied by " + str(multiple) + ".")
else:
    print("The number " + user_input + " is not a multiple of 10.")
