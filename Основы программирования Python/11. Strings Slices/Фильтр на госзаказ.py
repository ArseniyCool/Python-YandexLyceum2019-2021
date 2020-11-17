# Программа показывает работу какого-то сайта, фильтруещего сообщения методу,указываемому самим пользователем:
n = int(input())
m = input('Введите "#" - удаление, "%"- частичное удаление, "z" - замена: ')
zamena = 0
if m == 'z':
    zamena = input('Введите замену: ')
symbols = input('Введите начальные символы: (3 элемента):  ')
for i in range(1, n + 1):
    s = input()
    if s[:3] == symbols and m == '%':
        print(s[2:])
    elif s[:3] == symbols and m == 'z':
        print(zamena + s[3:])
    elif s[:3] != symbols and m == '#':
        print(s)
