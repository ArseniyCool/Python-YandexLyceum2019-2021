# Программа создаёт новогоднюю ёлку,
# состающую из поочерёдных чисел и украшенную новогодними шариками
height = int(input('Введите число шариков:'))
counter = 1
length = 1
while counter <= height:
    for i in range(0, length):
        print(counter, end=' ')
        counter += 1
        if counter > height:
            break
    length += 1
    print('')
