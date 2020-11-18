# Программа - типичная простейшая поисковая система с возможностью ввести несколько поисковых строк
n = int(input('Количество строк: '))
spisok = []
search = []
itog = []
# Cтроки с данными
for i in range(n):
    spisok.append(input())
n = int(input('Количество поисковых строк: '))
# Поисковые строки с данными
for i in range(n):
    search.append(input())
for i in spisok:
    trust = False
    for j in range(len(search)):
        if search[j] in i:
            trust = True
            continue
        trust = False
        break
    if trust:
        itog.append(i)
for e in itog:
    print(e)
