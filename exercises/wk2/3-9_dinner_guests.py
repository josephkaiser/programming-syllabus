guest_list = []
guest_list.append('Steve McQueen')
guest_list.append('Jesus Christ')
guest_list.append('Mahatma Ghandi')
guest_list.append('Abraham Lincoln')
guest_list.append('Norm MacDonald')
guest_list.append('Winston Churchill')
guest_list.append('Neil Armstrong')

while len(guest_list) > 0:
    print(f"We are inviting {len(guest_list)} people to dinner.")
    print("They are:")
    for i in guest_list:
        print(guest_list.index(i) + 1, i)
    
    popped_guest = guest_list.pop()
    print(f"Oh no! {popped_guest} can't make it!")
