

# x = []

# original_list = [34, 57, 81, 92, 2, 13]
# even_list_of_num = [x for x in original_list if original_list %2 ==0]
# print(even_list_of_num)

''' Exercise:

Write a 2D list that is a 3x3 grid of numbers
Write some code that prints out that grid nicely wither proper formatting.



# you are given a 2D list representing a table of data rows and columns .
# write a script to calculate the sum and average of each column in the table.

data = [[34, 54, 65],[78, 56, 45],[56, 45, 34]]
counter = 1
sum = 0
for row in data :
    for column in row:
        print(column)
        sum += column
        ave =sum/3
    print(f'counter: {counter} sum : {sum} ave: {ave} ')
    counter += 1
print('')

''' creating a list via for loop vs list comprehension
let's say you have a list of vegetable, and you want a new list containing only the vegetables that are less than 6 letters long.
''' 
# for loop

vegetable = ['broccoli', 'kale', 'onion', 'garlic', 'kale']
new_list_of_vegetable = []
for v in vegetable:
    if len(v) < 6:
        new_list_of_vegetable.append(v)
print(new_list_of_vegetable)
  
   
