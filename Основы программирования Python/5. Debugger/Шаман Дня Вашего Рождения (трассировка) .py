# Вычисление дня недели Вашего рождения
d = int(input())
m = int(input())
y = int(input())
c = 0
# Проверка високосности, от которой зависит многое
if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
    print("Високосный")
    if m == 1:
        m = 5
    elif m == 2:
        m = 6
    else:
        m = m - 2
else:
    print("Невисокосный")
    if m == 1:
        m = 8
    elif m == 2:
        m = 9
    else:
        m = m - 2
if y >= 100:
    c = y // 100
    y = y - c * 100
else:
    c = 0
week = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777))
print('---', week)
week2 = week % 7
print('Вы родились в', week2, 'день недели')
