'''
Expanded on basic concept in PythonCrashCourse chapter 5 voting.py pg. 83 to include user input and input validation as well as a wide range of accepted responses.
'''

age_lower_bound = 0
age_upper_bound = 200

print("What is your age in years?")
user_age = None
while True:
    user_age = input(" > ")
    
    try:
        '''Ensure stripped user age integer convertible'''
        user_age = int(user_age.strip())
        if not (age_lower_bound < user_age < age_upper_bound):
            print("Invalid age value!")
            continue
        else:
            break
    except ValueError:
        continue

# Give user many options for responses vs. just "y" or "n"
affirmative_responses = ['y', 'yes', 'aye', 'yay', 'true', 'indeed', 'ya', 'ye']
negative_responses = ['n', 'no', 'nye', 'nay', 'false', 'naw', 'noo', 'nah', 'na']

if user_age >= 18:
    print("User is old enough to vote!")
    print("Have you registered to vote yet? (y/n)")
    voter_status = None
    

    while voter_status != 'y' or voter_status != 'n':
        '''voter registration response while loop'''
        voter_status = input(" > ")
        voter_status = voter_status.lower().strip()
        if voter_status in affirmative_responses:
            print("Yippee!")
            break
        elif voter_status in negative_responses:
            print("Sorry, you are too young to vote")
            break
        else:
            continue

elif user_age < 18:
    age_delta = 18 - user_age
    print(f"Check back in {age_delta} years!")

else:
    exit
