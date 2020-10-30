# По задаче:
#  "Напишите программу, которая отгадывает загаданное целое число от 1 до 1000
#  (пользователь загадывает число в уме и не сообщает программе).
#  Угадать число нужно не более чем за 10 попыток. На каждую попытку пользователь отвечает,
#  что названное число больше загаданного (вводит символ “>”),
#  меньше загаданного (“<”) или угадано правильно (“=”)"
interval_max = int(input('Введите интервал максимальным числом до 1000:'))
hint = ''
interval_min = count = 0
while 1000 >= interval_max >= 1 and hint != '=':
    interval_between = (interval_min + interval_max) // 2
    print('---', interval_min, interval_between, interval_max)
    print(interval_between)
    hint = input()
    if hint == "<":
        interval_max = interval_between
    elif hint == ">":
        interval_min = interval_between
    count += 1
print('Ваше число отгадано за', count, 'попыток!')
