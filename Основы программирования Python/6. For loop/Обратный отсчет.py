n = int(input('Через сколько секунд запустить программу?:'))
i = 0
for i in range(0, n + 1):
    print('Осталось секунд:', n)
    n -= 1
print('Пуск!')
