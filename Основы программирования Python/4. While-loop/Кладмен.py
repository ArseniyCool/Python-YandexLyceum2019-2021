# Описание игры:
#  Вы находитесь на острове, на котором закопан клад. Изначально, Вы находитесь
#  в точке с координатами (0, 0) и смотрите на север. Вам известно местонахождение клада,
#  но этого мало: остров полон опасностей, и нужно перемещаться строго по указаниям Вашей карты,
#  дабы не быть съеденым аллигатором или пойманым в ловушку туземцами, или что по хуже...
#  При этом гарантировано,что карта приводит к кладу

#  Вы хотите найти клад как можно скорее,поэтому,если Вы найдёте клад раньше,
#  чем кончатся указания карты,Вы не дочитывая их,примитесь за раскопку клада

# P.S Чтобы игра была наглядней пользуйтесь координатной плоскостью

# Программа выводит минимальное кол-во указаний карты :
# действия («Вперёд» не считается)/шагов в одном направлении,
# требуемых до достижения клада и направление взгляда в этот момент
cord_x = int(input('Введите координату x - место,где закопан клад:'))
cord_y = int(input('Введите координату y - место,где закопан клад:'))
direct = input('Введите действие:')
# Возможные действия:
#  1) Пойти в данном направлении:
#     «вперёд»:
#       Возможные шаги:
#       - Любое целое(!) число
#  2) Изменить направление:
#  «налево», «направо», «разворот»
#  3) Cигнал остановки:
#     «стоп»
x = 0
y = 0
way = 'север'
count = 0
while (cord_x != x and cord_y != y) or direct != 'стоп':
    if direct == 'вперёд':
        direct = input('Введите кол-во шагов в заданном направлении:')
        if way == 'север':
            y += int(direct)
        elif way == 'юг':
            y -= int(direct)
        elif way == 'запад':
            x -= int(direct)
        elif way == 'восток':
            x += int(direct)
        count += 1
    else:
        if way == 'север':
            if direct == 'налево':
                way = 'запад'
            elif direct == 'направо':
                way = 'восток'
            elif direct == 'разворот':
                way = 'юг'
        elif way == 'юг':
            if direct == 'налево':
                way = 'восток'
            elif direct == 'направо':
                way = 'запад'
            elif direct == 'разворот':
                way = 'север'
        elif way == 'запад':
            if direct == 'налево':
                way = 'юг'
            elif direct == 'направо':
                way = 'север'
            elif direct == 'разворот':
                way = 'восток'
        elif way == 'восток':
            if direct == 'налево':
                way = 'север'
            elif direct == 'направо':
                way = 'юг'
            elif direct == 'разворот':
                way = 'запад'
        count += 1
        direct = input('Введите действие:')
print('Вам потребовалось', count, 'указаний карты, чтобы найти клад')
print('Вы смотрите на', way)
