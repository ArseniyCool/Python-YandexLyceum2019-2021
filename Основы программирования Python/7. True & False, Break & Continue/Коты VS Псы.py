# Программа считывает предложения и ищет слово "кот" и "пёс",иллюстрируя войну котов и собак.
# Если хотя бы в одной введённой строке нашлось сочетание букв «Кот» или «кот», коты лидируют в войне;
# однако если в этой или любой последующей строке нашлось сочетание букв «Пёс» или «пёс», то теперь лидируют псы
# После сигнала остановки - "СТОП" -
# выводит "Мяу" при поьеде котов,иначе "ГАВ" - при победе псов
n = int(input('Введите кол-во строк:'))
mew = False
for i in range(1, n + 1):
    line = input()
    if 'Кот' in line or 'кот' in line:
        mew = True
    if 'Пёс' in line or 'пёс' in line:
        mew = False
if mew:
    print('МЯУ')
else:
    print('ГАВ')
