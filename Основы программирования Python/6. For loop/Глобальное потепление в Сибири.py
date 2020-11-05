t = float(input('Вводите температуру до потепления(22℃):'))
count_day = 0
count_week = 0
while t <= 21.9:
    t = float(input())
    count_day += 1
    if count_day == 7:
        count_week += 1
        count_day = 0
print('Потепления произошло на', count_week, 'неделе')
