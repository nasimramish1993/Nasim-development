# import re


# while True:
 
 
#     choice = input("Choose 1, 2, or 3 parameters for your range: ")
 
 
#     if choice == '1':
#         start_1 = int(input("How long is your range: "))
#         output_1 = range(start_1)
#         for o in output_1:
#             # print(o, end=' ')
#         break
 
#     if choice == '2':
#         start_2 = int(input("How long is start value: "))
#         stop_2 = int(input('What is your stop value: '))
#         output_2 = range(start_2, stop_2)
#         for o in output_2:
#             # print(o, end=' ')
#         break




# Imports our regular expression module
 
# Problem: I need to test string data from a user input
# Solution: Regular expression can be used to see if a string contains a specific pattern
# '"In theory, you can substitute Regex with basic string operations or different operations with various libraries. The question remains why you would want to do this as it is way more code and way more effort."
 
# The Search function
 
# Metacharacters
# Starts with ^
# Ends with $
 
# Find a string with 7 characters starts with a g and ends with an e
 
import re


animal = 'giraffe'
result = re.search("^g.....e$", animal)
print(result)
 
 
# How does this look in an if statement?
 
if result:
    print("We have a match")
else:
    print("Sorry no match")
 
 
# How does this look in a ternary operator?
 
print("We have a match" if result else "Sorry no match")
 
#I wish to match  any of the letters 'bde' in a string, let's use square brackets.
 
teststring = 'Happy birthay to Quincy Jonesbde'
my_match = re.search('[bde]', teststring)
 
print(my_match)