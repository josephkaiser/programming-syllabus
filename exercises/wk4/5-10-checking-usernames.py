'''
5-10-checking-usernames.py
'''

# Initial data of usernames
current_users = ['admin', 'user1',' user2', 'user3', 'user4','user5','old1', 'old5','JOHN']
new_users = ['old1', 'new2', 'new3','new4','old5', 'john']

# Standardize to lowercase for uniqueness
current_users = [user.lower() for user in current_users]
new_users = [user.lower() for user in new_users]

# Check for usernames in both lists and handle logic if in or not in
for username in new_users:
    if username in current_users:
        print(f"{username} will have to enter a new username")
    else:
        print(f"{username} is available")
