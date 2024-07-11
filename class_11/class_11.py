

x = []

original_list = [34, 57, 81, 92, 2, 13]
even_list_of_num = [x for x in original_list if original_list %2 ==0]
print(even_list_of_num)

''' Exercise:

Write a 2D list that is a 3x3 grid of numbers
Write some code that prints out that grid nicely wither proper formatting.
'''

lis = [[1,2,3], [4,5,6], [7,8,9]]

for row in lis :
    print(row)
    for column in row :
        print(column, end= ' ')
        print('')