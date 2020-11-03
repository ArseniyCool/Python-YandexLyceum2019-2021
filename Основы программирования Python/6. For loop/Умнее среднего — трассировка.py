# Программа считывает IQ людей подряд,сравнивает IQ данного человека со средним до него IQ людей и выводит...:
#  0 - если IQ совпадает
#  > - если IQ выше
#  < - если IQ ниже
n = int(input('Введите кол-во участников:'))
i = 1
IQ_all = 0
IQ_center = 0
for i in range(1, n + 1):
    IQ = int(input())
    IQ_all += IQ
    IQ_center = IQ_all / i
    print('---', IQ_center)
    if IQ == IQ_center:
        print('0')
    elif IQ > IQ_center:
        print('>')
    else:
        print('<')
print('Cреднее IQ всех участников:', IQ_center)
