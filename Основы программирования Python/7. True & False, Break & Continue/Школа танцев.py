# В танце очень важно чувствовать ритм музыки.
# Программа проверяет, правильно ли ученик отсчитывает:
# раз, два, три, четыре, раз, два, три, четыре...
# При этом у учителя есть ограниченный запас терпения, и после определённого числа ошибок он заканчивает занятие.
n = int(input('Введите запас терпения учителя:'))
i = 0
count = 1
teacher = False
counter = 0
while i != n:
    time = input()
    if count == 1 and time == 'раз':
        teacher = True
    elif count == 2 and time == 'два':
        teacher = True
    elif count == 3 and time == 'три':
        teacher = True
    elif count == 4 and time == 'четыре':
        teacher = True
        count = 0
    else:
        teacher = False
    count += 1
    if teacher:
        counter += 1
    else:
        print('Правильных отсчётов было', str(counter) + ',', 'но теперь вы ошиблись.')
        counter = 0
        count = 1
        i += 1
print('На сегодня хватит.')
