# Пользователь вводит целые числа, ноль — сигнал остановки.
# Программа выводит кол-во чисел, которое было введено к моменту,
# когда сумма введённых чисел окажется равной 10(в первый раз)
# Если такого не было - выводит -1
num_all = 0
count = 0
count_TF = True
while True:
    num = int(input())
    if 0 == num:
        break
    num_all += num
    if count_TF:
        count += 1
    if num_all == 10:
        count_TF = False
if count_TF:
    print('-1')
else:
    print(count)
