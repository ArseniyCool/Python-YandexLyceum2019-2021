login = input('Enter login:')
email = input('Enter email:')
if '@' in login:
    print('Incorrect login')
elif '@' not in email:
    print('Incorrect email')
else:
    print('OK')
