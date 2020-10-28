one = input('Введите пароль:')
two = input('Подтвердите пароль:')
count = 0
while len(one) < 8 or "123" in one or one != two:
    if len(one) < 8:
        print('Короткий!')
    elif "123" in one:
        print('Простой!')
    elif one != two:
        print('Различаются.')
    one = input('Введите пароль:')
    two = input('Подтвердите пароль:')
