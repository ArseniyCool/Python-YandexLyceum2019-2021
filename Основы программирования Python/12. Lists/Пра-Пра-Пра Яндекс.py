# Программа - типичная простейшая поисковая система
n = int(input('Количество строк: '))
spisok = []
# Cтроки с данными
for i in range(n):
    line = input()
    spisok.append(line)
# Поисковая строка
line = input()
for i in spisok:
    if line in i:
        print(i)
