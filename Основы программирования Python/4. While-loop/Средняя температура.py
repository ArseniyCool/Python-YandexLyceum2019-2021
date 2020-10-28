t = float(input('Введите температуру:'))
t_all = 0
count = 0
while 300 >= t >= -300 or t == "стоп":
    t_all += t
    count += 1
    t = float(input('Введите температуру:'))
t_all /= count
print('Вот средняя температура:', t_all)
