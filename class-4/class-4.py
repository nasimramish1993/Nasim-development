# print('class four')

# Bname = 'Abdulkhaliq'
# if Bname == 'Abdulkhaliq':
#     print('Hello my sweet brother')

# user_name = input('please enter the tempreture: ')
# user_name = int(user_name)
# if user_name > 60 :
#     print('it is too hot')

# elif user_name  > 45 :
#     print('the weather is normal')
# else:
#         print('it is too coold')

# userin = input('Enter your numbers: ')
# userin = int(userin)
# if userin % 2 != 0:
#     # print(f'{userin} is odd')

# userin = input('Enter your numbers')
# userin = int(userin)
# print(f'{userin} is even')
# if userin % 2 == 0:
#     # print(userin)

# userin = input('please enter your numbers: ')
# userin = float(userin)

# if userin % 2 == 1:
#     print(f'{userin} is odd')
# elif userin % 2 == 0:
#     print(f'{userin} is even')
# else:
#     print('unknown')

   # checking for somethings 
# userin = input('Enter your text: ')
# if userin.isdecimal():
#     print('this is number')
# elif userin.isalpha():
#     print('this is words')

# else:
#     print(' somethig else')

Name = ['sadiq', 'nasim', 'Azar']

Name.append('Abdulali')
# print(Name)

months = ['june', 'july']
months.clear()
# print(months)

copy_me = [1, 2,3]
new_copy = copy_me.copy()
print(new_copy)
# print(type(new_copy))

lest = ['apple', 'orange', 'apple']
# print(lest.count('apple'))

New_users = ['ali', 'nasir',]
current_users = ['nasim','nasim', 'sadiq']
current_users.extend(New_users)
# print(current_users)

num_sort = [1,4,2,3,6]
num_sort.sort()
# print(num_sort)

''' 

Create a for loop that goes through a list and prints each item in the list, along with its index. (Hint: Create a separate counter variable to keep track of the index.)

Example:
planets = ["mercury", "venus", "earth", "mars"]
0: mercury, 1: venus, 2: earth, 3: mars
 '''

counter = 0
output = ''

Names = ['ali','nasim', 'sadiq']

for N in Name:
    Num_and_index = f"{counter} : {N} "
    output += Num_and_index
    counter += 1
# print(output)

for i in range(3,2):
#   print(i)

  for i in range(1960, 2001,-5):
   print(i, end=', ')