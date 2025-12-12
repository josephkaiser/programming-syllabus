'''
5-8-hello-admin.py
Python Crash Course
Chapter 5
Exercise 8
'''

usernames = ['admin', 'joe', 'maya', 'bunny', 'geeunit']
'''print a greeting to each user after they log in to a website'''
if usernames:
    for username in usernames:
        if username == 'admin':
            print("Hello, admin. Would you like to see a status report?")
        else:
            print(f"Hello, {username}, thank you for logging in again.")
else:
    print("Error! No usernames.")
