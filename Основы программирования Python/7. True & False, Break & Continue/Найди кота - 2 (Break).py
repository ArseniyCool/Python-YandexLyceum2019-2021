# Программа считывает предложения и ищет слово "кот".После сигнала остановки - "СТОП" или в момент когда найден "кот" -
# выводит номер предложения,в котором было найдено это слово,иначе -1
mew = False
count = True
i = 1
cat = 0
while True:
    line = input()
    if ('Кот' in line or 'кот' in line) and count:
        mew = True
        cat = i
        count = False
        break
    if 'СТОП' in line:
        break
    i += 1
if mew:
    print(cat)
else:
    print('-1')
