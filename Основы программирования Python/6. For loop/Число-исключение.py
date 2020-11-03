# Программа перемножает 7 введённых чисел
# Кроме числа-исключения
i = 1
num_all = 1
num_exc = int(input('Введите число-исключение:'))
for i in range(1, 7):
    num = int(input('Введите число:'))
    if num != num_exc:
        num_all *= num
    i += 1
print(num_all)
