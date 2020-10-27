# Программа выстраивает людей по росту
a = int(input('Введите рост первого человека:'))
b = int(input('Введите рост второго человека:'))
c = int(input('Введите рост третьего человека:'))
if a > b and a > c:
    if b > c:
        print(str(a, "см"))
        print(str(b, "см"))
        print(str(c, "см"))
    else:
        print(str(a, "см"))
        print(str(c, "см"))
        print(str(b, "см"))
elif b > a and b > c:
    if a > c:
        print(str(b, "см"))
        print(str(a, "см"))
        print(str(c, "см"))
    else:
        print(str(b, "см"))
        print(str(c, "см"))
        print(str(a, "см"))
elif c > a and a < b:
    print(str(c, "см"))
    print(str(b, "см"))
    print(str(a, "см"))
else:
    print(str(c, "см"))
    print(str(a, "см"))
    print(str(b, "см"))
