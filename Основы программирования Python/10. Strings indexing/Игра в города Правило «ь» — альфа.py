# Игра в города в один раунд:
#  Участники вводят поочередно 2 города(1 раз),
#  так чтобы каждая начальная буква города начиналась с конечной буквы прошлого города, при этом используется
#  правило мягкого знака(В городе,оканчивающимя на "ь", берётся предпоследняя буква),
#  если один из участников ошибётся - он проиграет(Сигнал остановки) и программа выведет последнее слово
#
# Города писать в нижнем регистре
word_1 = input()
word_2 = input()
count = 'do not know'
if (word_1[len(word_1) - 1] == chr(1100)) and (word_1[len(word_1) - 2] == word_2[0]):
    count = True
elif word_1[len(word_1) - 1] == word_2[0]:
    count = True
else:
    count = False
if count:
    print('ВЕРНО')
else:
    print('НЕВЕРНО')
