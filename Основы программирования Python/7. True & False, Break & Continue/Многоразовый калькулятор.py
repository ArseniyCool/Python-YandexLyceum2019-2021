# «+» (сложить два числа),
# «-» (вычесть из первого числа второе),
# «*» (перемножить два числа),
# «/» (поделить первое число на второе нацело),
# «%» (получить остаток от деления первого числа на второе),
# «!» (посчитать факториал от первого числа, ввод второго числа не производится),
# «x» (вывести первое число и закончить выполнение программы, ввод второго числа не производится).
two = 'nothing'
while True:
    one = int(input())
    sign = input()
    if sign == '!' and one > 0:
        i = 2
        for i in range(2, one):
            one *= i
            i += 1
        print(one)
    elif sign == '!' and one == 0:
        print(one + 1)
    elif sign == 'x':
        print(one)
        break
    elif sign != '!':
        two = int(input())
    if sign == '+':
        print(str(one + two))
    elif sign == '-':
        print(str(one - two))
    elif sign == '*':
        print(str(one * two))
    elif sign == '/' and two != 0:
        print(str(one // two))
    elif sign == '%' and two != 0:
        print(str(one % two))
    elif sign == 'x':
        print(one)
        break
