# По задаче:
#  Последовательность чисел Фибоначчи описывает размножение кроликов, рост веток на деревьях и много чего ещё.
#  Определяется последовательность так: первый и второй члены последовательности равны 1,
#  а каждый последующий — сумме двух предыдущих. Напишите программу, которая выводит первые несколько членов
#  последовательности Фибоначчи — все, не превышающие натурального числа, заданного пользователем.
num = int(input('Введите конечное число,до которого будет выведена последовательность чисел фибоначчи'))
a = b = 1
while a <= num and b <= num:
    print(a)
    print(b)
    a = a + b
    if a + b <= num:
        b = a + b
        if a + b > num:
            print(a)
    print(a)
