# Программа определяет, является ли данное число произведением двух чисел из данного набора,
# и выводит «ДА» или «НЕТ» в зависимости от этого.

# Если число в наборе одно, само на себя умножиться оно не может,т.е. два множителя должны иметь разные номера в наборе.
n = int(input('Кол-во чисел: '))
elem_set = list()
trust = False
# n чисел
for i in range(n):
    elem = int(input())
    elem_set.append(elem)
composition = int(input('Введите число, проверку множителей которого Вы хотите выполнить:'))
for i in range(0, len(elem_set)):
    if trust:
        break
    for j in range(1, len(elem_set)):
        if elem_set[i] * elem_set[j] == composition:
            trust = True
            break
if trust:
    print('ДА')
else:
    print('НЕТ')
