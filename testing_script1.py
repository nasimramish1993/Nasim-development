# divide by 3
pizza_slices = 44
pizza_slices /= 3
print(pizza_slices)


# find the reminder if divided by 3?
hours = 24
day_of_the_week ='tuesday'

# formatted strige 

print(f'there are {hours} hours. happy {day_of_the_week} !')

# cancatenation
first_name = 'nasim'
last_name = 'muhsiny'
full_name = first_name + ' ' + last_name
print(full_name)

# multiplacation 
greeting = 'jon hon nasim '
three_cheers = greeting  * 3
print(three_cheers)

fav_food = 'Apple '
result = fav_food * 10
print(result)

# is 'a' in "girrafe" ?
print( 'a' in 'girrafe')

# is 'z' in birthday ?
print('z' in 'birthday')

# is 's' in school ?
print('s' in 'school')

# is 'w' in wrapper ?
print('w' in 'wrapper')
print('W' in 'wrapper')

# pardon
pardon_length = len('pardon')
print(pardon_length)

# muhsniy
muhsiny_length = len('muhsiny')
print(muhsiny_length)

# capitalize() convert the first chracter in to lower case
name = 'nasim'
print(name.capitalize()) 

color = 'blue'
print(color.capitalize())

# confoled() convert string in to lower case 
num_one = 'nAsim'
num_tow = 'nasim'
print(num_one==num_tow)

# lower case every letter of string
print(num_one. casefold())
print(num_tow. casefold())
# let's check it again it will return it true now
print(num_one.casefold() == num_tow.casefold())

# center () print string centered 100
print('Hello'.center(100))

# count() 
my_string = 'cancatation' 
letter_count = my_string.count('a')
print(letter_count)
# cancatation 
first_name = 'Nasim '
last_name = 'Muhsiny'
full_name = first_name + '' + last_name
print(full_name)

# expandtabs 
testing_tabs = 'hello\thappy\ttuesday'
print(testing_tabs)

two_charts = testing_tabs.expandtabs(2)
print(two_charts)

three_cheers = testing_tabs.expandtabs(3)
print(three_cheers)

# find the position of letter n in nasim
name = 'nasim'
n = name.find('nasim')

find_letter_n = (f'the letter "n" which appears at index {n} in {name}')
print(find_letter_n)

a = 'apple'
find_letter_a = a .find('a')
print(find_letter_a)
print(f'the letter "a" which appears at index {find_letter_a} in {a}')

f = 'define'
find_letter_f = f.find('f')
print(find_letter_f)
print(f'the letter "f" which appears at index{find_letter_f} in {f}')

day = 'monday'
n = day.find('n')
print(n)
print(f'the letter "n" which appears at index {n} in {day}')

fruit = 'orange'
x = fruit.find('orange')
print(x)
print(f'the letter "x" which appears at index {x} in {fruit}')


# isalnum() return true if it alphanomaric also return true
word_one = '@#$%^'
word_two = 'asdfdj'
word_three = '123asdf'
print(word_one.isalnum())
print(word_two.isalnum())
print(word_three.isalnum())

# isalpha() is alpha similar to but only alphatical isalpha
word_one = 'afdkjfd'
word_two =  '122jkjda'
word_three = '!@#jfskj234'

print(word_one.isalpha())
print(word_two.isalpha())
print(word_three.isalpha())

# isdigits() return true if all chractars in the string are digits

num_one = '23456'
num_tow = '4.345'
num_three = 'wert'

print(num_one.isdigit())
print(num_tow.isdigit())
print(num_three.isdigit())

# islower() return true if all chracters in the string are lower case

house_name = 'Masjid'
name_of_street = 'shahed-mazari'
print(house_name.islower())
print(name_of_street.islower())

# istitle() return true if the first chractar of string is in capitalized
w1 = 'Nasim'
w2 = 'Muhsiny'
print(w1.istitle())
print(w2.istitle())

first_letter_of_word = 'nasim'
result = f'nasim'. index(first_letter_of_word)
print(result)
age1 = 25
age =+ 5
result = age1+age
print(result)
