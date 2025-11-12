guest_list = []
guest_list.append('Steve McQueen')
guest_list.append('Jesus Christ')
guest_list.append('Mahatma Ghandi')
guest_list.append('Abraham Lincoln')
guest_list.append('Norm MacDonald')
guest_list.append('Winston Churchill')
guest_list.append('Neil Armstrong')

# for i in guest_list:
#     print(f"{i}, you are cordially invited to a dinner party Saturday night")

print("Uh oh! Jesus Christ can't make it!")

bob = guest_list.pop(1)
guest_list.insert(1, 'Magic Johnson')

print("We've found a bigger dinner table")

guest_list.append('Slowmo Joe')
guest_list.insert(0, 'Johny Lately')
guest_list.insert(int(len(guest_list)/2), 'Becky Midster')

for i in guest_list:
    print(f"{i}, you are cordially invited to a dinner party Saturday night")
