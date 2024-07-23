

''' Fun facts about dictionaries 

    -collection of keys and values
    -used to store associated information
    -keys are the words, values are the definitions

'''

# How do we create a dictionary?




# Bracket notation - we can grab the value by referencing the key


# # Add new key/value pair


# lets look at all the methods available to us


# lets try one


# Dict constructor


# Let's update our name key



# Dictionary methods
# Lets use the keys methods to get the keys from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Let's look at our keys
print(f'the key for the dog dictionary are {dog.keys()}')
# or set it as a variable?
dog_new = {}
dog_new= dog.keys()
# print(dog_new)



# Lets use the values methods to get the values from this dictionary

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

# Lets look at our values
# print(f'the value for the dog dictionary are {dog.values()}')

# or set to a variable
dog_values = dog.values()
# print(dog_values)
# Lets use clear method to remove all elements

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}
dog.clear()
# print(dog)

# Lets use get method to get a key value

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}
# print(dog.get("age"))
# print(dog.get('nasim'))


# lets look at one of the parameters to show an error if the key doesnt exist
# print(dog.get('breed'))
# print(dog.get('nasim', 'this peramiter does not exist in dictionary'))


# Lets create a copy

dog = {
    "breed": "japanese chin",
    "gender": "female",
    "age": 7
}

dog_copy = dog.copy()
# print(dog_copy)

# Lets remove a specified key with pop
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}
dog.pop('breed')
# print(dog)
gender = dog.pop('gender')
print(gender)
# print(dog)

# Lets remove a last inserted key-value pair with popitem
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}
dog.popitem()
# print(dog)

# Get a list with each key-value pair with items
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}
new_list = dog.items()
# print(new_list)



# we can loop through
dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}
for key , value in dog.items():
    # print(key, value, end= '/')



# Update dictionary
 dog = {
    "breed": "japanese chin",
    "gender": "male",
    "age": 7
}

dog.update({'name': 'nasim'})
# print(dog)




# Update can also update current key value pairs, as well as adding



# Dictionaries vs Lists
list1 = ['a', 'b', 'c', 'd', 'e']
dict1 = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 5: 'e'}
# print(list1[0])
# print(dict1[2])
add_name = {'nasim': 'muhsiny'}
dict1.update({'nasim': 'muhsiny'})
# print(dict1)

dict1[2]= 'nasim'
# print(dict1)
'''
Write some code that takes two lists and converts them into one dictionary.
In:
list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]
Out:
{'one': 4, 'two': 10, 'three': 30}

'''

list1 = ['one', 'two', 'three']
list2 = [4, 10, 30]

dict3 = {}
for m in range(len(list1)):
    dict3[list1[m]]= list2[m]
print(dict3)



''' Zip Solution

When you use the zip() function in Python, it takes two or more data sets and "zips" them together. This returns an object containing pairs of items derived from the data sets. 
'''

my_keys = ['one', 'two', 'three']
my_values = [4, 10, 30]

# create an empty dictionary to add key value pair into 

dict1 = {}

for m in range(len(my_keys)):
    dict1[my_keys[m]] = my_values[m]
# print(dict1)

dict1 = dict(zip(my_keys, my_values))
# print(dict1)





'''
Exercise

Write a dictionary that five countries and their languages Then have your code print the languages of each country one at a time.
Hint: Use the items() method


'''

languages = { 'USA': 'English', 'Mexico': 'Spanish', 'France': 'French', 'Portugal':'Portugese', 'Belgium':'Dutch' }
    
country = ''
language = ''
# for country , language in languages.items():
# print(f'the language of {country}, is {language}')

# As datasets, we can use bracket notation

choices = {"flavors":['strawberry', 'vanilla', 'orange'],
           "sizes":['large', 'medium', 'small']}
strawbarry = choices["flavors"][0]
vanilla = choices["flavors"][1]
orange = choices["flavors"][2]
 
large = choices["sizes"][0]
medium = choices["sizes"][1]
small = choices["sizes"][2]
# print(strawbarry, vanilla, orange)
# print(small, medium,large)
# Lets make a dataframe out of this
import pandas as pd 
choices.update({'vehicals': ['kia', 2012, 'white']})
choices_df = pd.DataFrame(choices)
print(choices_df)

# Lets rename the columns




'''
Exercise
Create a dictionary for an automobile including make, model, year, number of doors, and number of cylinders.
'''
vehicals = {'year': [2011 , 2012 ,2013 ,2024],
            'model': ['kia', 'honda', 'accord', 'soburo'],
             'number': [1234, 345, 345, 345678] }
vehical_new_list = {}
import pandas as pd 

vehicals.update({'num plate': [21345, 123456 , 45678, 3456]})

vehical_new_list = pd.DataFrame(vehicals)
print(vehical_new_list)

'''
In statistics, the mode is the value that appears most frequently in a dataset.
For example, in this list: [1,2,4,1,3,4,1,1] the mode is 1
Write some code that uses a dictionary to calculate the mode of a list.

'''

my_list_items = [1,2,4,1,3,4,1,1] # our list

output = {}
for m in my_list_items:
    if m not in output:
        output[m] =1
    else:
        output[m] +=1
# print(output)



# What about the count method for Lists?? 

for m in my_list_items:
    output[m]= my_list_items.count(m)
# print(output)


# from statistics import mode
from statistics import mode
result = mode(my_list_items)
# print(f'the mode is {result}')

'''
Suppose you have a list of employee records that contain the following information for each employee: name, job title, salary. The records are stored as a list of dictionaries.
Use this list to create a dictionary where the keys are the job titles and the values are the average salaries for each job title.
Example:
records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},\
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},\
           {'name': 'David', 'title': 'developer', 'salary': 65000}]
Output: {'manager': 50000, 'developer': 62500}
'''

records = [{'name': 'Bob', 'title': 'manager', 'salary': 50000},
           {'name': 'Alice', 'title': 'developer', 'salary': 60000},
           {'name': 'David', 'title': 'developer', 'salary': 65000}]


manager_salaries = []
developer_salaries = []
output = {}

for person in records:
    if person['title'] == 'manager':
        manager_salaries.append(person['salary'])
    elif person["title"] == 'developer':
        developer_salaries.append(person["salary"])

developer_ave = 0
manager_ave = 0
for salary in manager_salaries:
    manager_ave += salary
    manager_ave /= len(manager_salaries)

for salary in developer_salaries:
    developer_ave += salary
    developer_ave /= len(developer_salaries)
output['manager'] = manager_ave
output['developer'] = developer_ave
# print(output)