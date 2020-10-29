circle = int(input('Введите круглое число:'))
while circle % 10 == 0:
    print(circle)
    circle = int(input('Введите ещё круглое число:'))
print(circle, '- не круглое число :(')
