# Программа считывает предложения и ищет слово "кот" и "пёс",иллюстрируя войну котов и собак.
# Каждый раз когда встречается "кот" количество очков и кошек увеличивается на 1,аналогично и в случае с псами
# После сигнала остановки - "СТОП" - выводит счёт котов и псов, и "Мяу" при победе котов
# (Если коты набрали больше очков,чем псы),иначе "ГАВ" - при победе псов, при равном счёте - "ЛЮДИ"
n = int(input('Введите кол-во строк:'))
mew_count = woof_count = 0
for i in range(1, n + 1):
    line = input()
    if 'Кот' in line or 'кот' in line:
        mew_count += 1
    if 'Пёс' in line or 'пёс' in line:
        woof_count += 1
print(mew_count, 'VS', woof_count)
if mew_count >= woof_count:
    print('МЯУ')
elif mew_count <= woof_count:
    print('ГАВ')
else:
    print('ЛЮДИ')
