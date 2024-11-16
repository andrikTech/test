print('login')
username = input('Insert your username')
password = input('Insert your password')

if username != 'admin' and password != '1234':
    print('Your username or password is incorrect')
else:
    print('You\'ve been logged in')
    print('Welcome')

