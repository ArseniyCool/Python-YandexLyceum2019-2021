# Игра в города в один раунд:
#  Участники вводят поочередно 2 города(1 раз),
#  так чтобы каждая начальная буква города начиналась с конечной буквы прошлого города,
#  если второй участник ошибётся - он проиграет
#
# Города писать в нижнем регистре
word_1 = input()
word_2 = input()
while word_1[len(word_1) - 1] == word_2[0]:
    print('---', word_1[len(word_1) - 1])
    print('---', word_2[0])
    print('--- Верно 1')
    word_1 = input()
    if word_2[len(word_2) - 1] != word_1[0]:
        print(word_1)
        break
    print('---', word_2[len(word_2) - 1])
    print('---', word_1[0])
    print('--- Верно 2')
    word_2 = input()
else:
    print(word_2)
print('---', word_1[len(word_1) - 1])
print('---', word_2[0])
print('--- Неверно')
