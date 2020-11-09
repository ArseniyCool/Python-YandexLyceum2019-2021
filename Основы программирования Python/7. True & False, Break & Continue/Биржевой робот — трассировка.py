# Программа для автоматической торговли акциями на бирже.
# Вводится цена акций в первый, второй и т. д. дни, ноль — сигнал остановки.

# Принцип работы:
#  Робот покупает акцию в первый день - когда цена акции превышает цену в предыдущий день. После этого в какой-то момент
#  цена акций начинает уменьшаться. Робот продаёт акции в первый же день, как только её цена становится меньше цены
#  в предыдущий день. Возможно, после этого цены как-то ещё меняются.

# Среди введенных цен точно должен быть день, когда цена начнет расти, а после день, когда цена начнет падать.
# Не следует пользоваться советами этого робота в реальной жизни)
share = int(input())
share2 = 1
sell = 1
buy = 1
buying = selling = False
go_sell = go_buy = True
count = True
way = 'not'
while 0 != share:
    share2 = int(input())
    if share > share2 and count:
        way = 'down'
        count = False
    elif share2 > share and count:
        way = 'up'
        count = False
    if share > share2 and go_buy and way == 'down':
        buying = True
    elif share2 > share and go_sell:
        selling = True
    if share > share2 and go_sell and way == 'up':
        selling = True
    elif share2 > share and go_buy:
        buying = True

    if selling and share > share2:
        sell = share2
        print('---', sell)
        selling = False
        go_sell = False
    if buying and share2 > share:
        buy = share2
        print('---', buy)
        buying = False
        go_buy = False
    share = share2
benefit = sell - buy
print('Покупка:', buy, '/ Продажа:', sell, '/ Прибыль:', benefit)
