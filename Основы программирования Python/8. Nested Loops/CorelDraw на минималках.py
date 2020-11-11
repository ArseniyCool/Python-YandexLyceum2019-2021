# Программа рисует прямоугольник указаной высоты,длины и символа(А что Вы хотели?)

# Вводите значения в указанном сверху порядке
h = int(input())
b = int(input())
sign = input()
n = ' ' * (b - 2)
for i in range(b):
    print(sign, end='')
print('')
for i in range(h - 1):
    if i == (h - 2):
        for j in range(b):
            print(sign, end='')
    else:
        print(sign, end=n)
        print(sign, end='\n')
