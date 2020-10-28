one = str(input('Введите пароль:'))
if len(one) >= 8:
    two = input('Подтвердите пароль:')
    if one == two:
        print('OK')
    else:
        print('Различаются.')
else:
    print('Короткий!')
