guest_list = []
guest_list.append('Steve McQueen')
guest_list.append('Jesus Christ')
guest_list.append('Mahatma Ghandi')
guest_list.append('Abraham Lincoln')
guest_list.append('Norm MacDonald')
guest_list.append('Winston Churchill')
guest_list.append('Neil Armstrong')

for i in guest_list:
    print(f"{i}, you are cordially invited to a dinner party Saturday night")

print("Uh oh! Jesus Christ can't make it!")


bob = guest_list.pop(1)
guest_list.insert(1, 'Magic Johnson')

for i in guest_list:
    print(f"{i}, you are cordially invited to a dinner party Saturday night")
