print('class five')


user_name = 'nasimmuhsiny'
password = 'nasim'
path_key = 'ghazni'

user_name1 = input('enter user name: ')
user_password = input('enter password: ')
key_words = input('where were you born: ')

if (user_name == user_name1 and user_password == password and key_words == path_key ):
    print('login is successfully')

elif (user_name != user_name1 and user_password == password and key_words == path_key ):
    print('enter key words')

else:
    print('you lost your account')

