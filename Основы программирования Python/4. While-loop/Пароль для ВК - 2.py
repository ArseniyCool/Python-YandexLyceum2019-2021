one = str(input())
if len(one) < 8:
    print('Короткий!')
elif "123" in one:
    print('Простой!')
else:
    two = input()
    if one == two:
        print('OK')
    else:
        print('Различаются.')
