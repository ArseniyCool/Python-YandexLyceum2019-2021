# Программ считает сумму товаров и делает скидку 5 % на товар,если его стоимость превышает 1000
price = float(input('Введите цену на товар:'))
cost = 0
while price >= 0:
    print(price, cost)
    if price > 1000:
        cost = cost + (price - 0.05 * price)
    else:
        cost = cost + price
    print(price, cost)
    price = float(input('Введите цену на товар:'))
    # Сигнал остановки - нуль или отрицательное число
print(cost)