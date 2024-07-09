# adding and indixing in a list through for loop
# append:
day = ['tuesday', 'wenseday']

day.append('friday')
# print(day)


#clear
day = ['tuesday','friday', 'wenseday']
day.clear()
# print(day)

#copy
day = ['tuesday','friday', 'wenseday']

new_daysn = day.copy()
# print(new_daysn)

#  count 

day = ['tuesday','tuesday', 'tuesday']

length_of_day = len(day)
# print(f'length of days : {length_of_day}')

count_of_days = day.count('tuesday')
# print(f'count of the days are : {count_of_days}')

# extend 

day = ['tuesday','tuesday', 'tuesday']
new_days = ['tuersday', 'friday']
new_days.extend(day)
print(f'new days are : {new_days}')

# index() Returns the index of the first element with the specified value

# name_of_friend = ['sadiq', 'ali', 'Muhammad']
# index = name_of_friend.index('ali')
# print(f'ali index : {index}')
# print(f'ali is in index {index+1}nd items in the list')

# pop() remove by index and remove() remove by value

name_of_friend = ['sadiq', 'ali', 'Muhammad']

name_of_friend.pop(2)
print(name_of_friend)

# name_of_friend.remove('sadiq')
# print(name_of_friend)


while True :
    user = input('what day is today? :').lower()
    if user=='monday':
        break
    else:
        print(f'Happy {user}')
        

