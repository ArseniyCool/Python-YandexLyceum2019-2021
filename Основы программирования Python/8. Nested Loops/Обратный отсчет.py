n = int(input('Время:'))
i = 0
j = 0
for i in range(n):
    for j in range(1 + i):
        print('Осталось секунд:', i - j)
    print('Пуск', j + 1)
