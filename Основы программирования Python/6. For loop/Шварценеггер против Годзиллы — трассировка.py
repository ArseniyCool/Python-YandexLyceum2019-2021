# Игра:
#  Эмулятор битвы с боссом по алгоритму Евклида

#  Вводится дробь(В первой строке числитель,в следующей знаменатель,
#  где знаменатель больше числителя) - количество урона нанесённого Годзилле
#  от общего количества её жизней
# Программа выводит дробь - общее кол-во нанесенного Годзилле урона
n = int(input('Введите количество ударов по Годзилле:'))
i = 1
znam_all = 0
chisl_all = 0
for i in range(1, n + 1):
    znam_x = znam_all
    chisl_x = chisl_all
    chislitel = int(input('Введите числитель:'))
    znamenatel = int(input('Введите знаменатель:'))
    if chisl_x == 0 and znam_x == 0:
        znam_x = znamenatel
    if znam_x == znamenatel:
        znam_all = znamenatel
        chisl_all = chislitel + chisl_x
    else:
        znam_all = znamenatel * znam_x
        chisl_all = chislitel * znam_x + chisl_x * znamenatel
    nod1 = znam_all
    nod2 = chisl_all
    while nod1 != nod2:
        if nod1 > nod2:
            nod1 -= nod2
        else:
            nod2 -= nod1
    chisl_all //= nod2
    znam_all //= nod1
    i += 1
    print('---', chisl_all, '/', znam_all)
print('Годзилле было нанесено:', chisl_all, '/', znam_all, sep='')
if chisl_all == znam_all:
    print('Вы убили Годзиллу!')
else:
    print('Вы убили Годзиллу! И даже престарались с выстрелами...')


