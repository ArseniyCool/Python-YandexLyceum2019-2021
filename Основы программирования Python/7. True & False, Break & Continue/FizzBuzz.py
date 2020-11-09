# Программа запрашивает ввод чисел(Где a < b) и проверяет каждое число в этом интервале,выводя:
#  - “Fizz”, если это число делится на 3;
#  - “Buzz”, если это число делится на 5;
#  - “FizzBuzz”, если выполнены оба предыдущих условия;
#  - само это число в остальных случаях.
a = int(input('Введите начало интервала:'))
b = int(input('Введите конец интервала:'))
i = a
for i in range(a, b + 1):
    Fizz = False
    Buzz = False
    FizzBuzz = False
    if i % 3 == 0:
        Fizz = True
    if i % 5 == 0:
        Buzz = True
    if Fizz and Buzz:
        print('FizzBuzz')
    elif Fizz:
        print('Fizz')
    elif Buzz:
        print('Buzz')
    else:
        print(i)
    i += 1
