# # adding and indixing in a list through for loop
# # append:
# day = ['tuesday', 'wenseday']

# day.append('friday')
# # print(day)


# #clear
# day = ['tuesday','friday', 'wenseday']
# day.clear()
# # print(day)

# #copy
# day = ['tuesday','friday', 'wenseday']

# new_daysn = day.copy()
# # print(new_daysn)

# #  count 

# day = ['tuesday','tuesday', 'tuesday']

# length_of_day = len(day)
# # print(f'length of days : {length_of_day}')

# count_of_days = day.count('tuesday')
# # print(f'count of the days are : {count_of_days}')

# # extend 

# day = ['tuesday','tuesday', 'tuesday']
# new_days = ['tuersday', 'friday']
# new_days.extend(day)
# print(f'new days are : {new_days}')

# index() Returns the index of the first element with the specified value

# name_of_friend = ['sadiq', 'ali', 'Muhammad']
# index = name_of_friend.index('ali')
# print(f'ali index : {index}')
# print(f'ali is in index {index+1}nd items in the list')

# pop() remove by index and remove() remove by value

# name_of_friend = ['sadiq', 'ali', 'Muhammad']

# name_of_friend.pop(2)
# print(name_of_friend)

# name_of_friend.remove('sadiq')
# print(name_of_friend)


# while True :
#     user = input('what day is today? :').lower()
#     if user==('monday'):
#       break
#     else:
#         print(f'Happy {user}')


# as you can see here , a list cam hold any data type as an item in the list. Even another list.
# i_can_hold_everythings = [4, 'nasim', True, ['nasim' , 'ali', 'sadiq'], {4,'Muhsiny', 4}, {'fname': 'Abdulazim'}]
# for item in i_can_hold_everythings:
#    print(f'index {i_can_hold_everythings.index(item)}: {item} type: {type(item)}')

# name = [ ]

# while True:
#    user = input('enter your name : ').lower()
#    if (user.lower() == 'stop'):
#       break
   
#    else: 
#       if user.lower() not in name:
#          name.append(user.lower())
#          print(name)
#       else:
#          print(f'{user} is already in the list! try again')
#          continue
# print(f'final list of name: {name}')


my_friends = [ ]

while True:
    user = input('who is your friends : ').lower()

    if user.lower() == 'stop':
        break
    else:
        if user.lower() not in my_friends:
            my_friends.append(user.lower())
            print(my_friends)
        else:
            print(f'{user.lower()}: is already in the list! tell me another one please')
            continue
print(f'final names of my friends: {my_friends}')
