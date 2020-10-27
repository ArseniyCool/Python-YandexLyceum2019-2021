one = float(input())
two = float(input())
sign = input()
if sign == '+':
    print(one + two)
elif sign == '-':
    print(one - two)
elif sign == '*':
    print(one * two)
elif sign == '/':
    if two != 0:
        print(one / two)
    else:
        print('(Ошибка 888888)')
else:
    print('(Ошибка 888888)')
