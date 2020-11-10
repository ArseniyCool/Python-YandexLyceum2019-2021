# Программа считывает предложения и ищет слово "кот".После сигнала остановки - "СТОП" -
# выводит общее количество строк, в которых были упомянуты это слово и номер предложения,
# когда был найден первый "кот" ,иначе - количество строк и -1
mew = False
count = True
i = 1
cat = 0
cat_times = 0
while True:
    line = input()
    if 'Кот' in line or 'кот' in line:
        mew = True
        if count:
            cat = i
        cat_times += 1
        count = False
    if 'СТОП' in line:
        break
    i += 1
if mew:
    print(cat_times, cat)
else:
    print(cat_times, '-1')
