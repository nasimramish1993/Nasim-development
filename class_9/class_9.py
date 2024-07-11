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


# my_friends = [ ]

# while True:
#     user = input('who is your friends : ').lower()

#     if user.lower() == 'stop':
#         break
#     else:
#         if user.lower() not in my_friends:
#             my_friends.append(user.lower())
#             print(my_friends)
#         else:
#             print(f'{user.lower()}: is already in the list! tell me another one please')
#             continue
# print(f'final names of my friends: {my_friends}')


'''Exercise : Removing all duplicates
you have a list storing important data for your company, but it contains some duplicate entires. Go through your list and remove all the duplicates . when you are done , each item should appear in the list exactly once .
Hint: how would you extend our previous example which remove duplicates of one value, to remove duplicates of all values?
Hint2 : you might want to make a copy of the original list to use as reference. you want to use more than one loop.  
'''

cities = ['Ghazni', 'Kabul', 'Herat', 'Kabul', 'Herat']
for item in cities.copy():
    print(f'index {cities.index(item)}: {item}')

    item_count = cities.count(item)
    print(f'item count: {item_count}\n\n')
    if item_count > 1 :
        cities.remove(item)
print(f'final list of cities Afghanistan: {cities}')


set_cities = set(cities)
print(set_cities)

new_list = list(set_cities)
print(new_list)
