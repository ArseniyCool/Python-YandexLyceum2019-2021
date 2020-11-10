# Программа считывает указанное число предложений,и если хоть в одном находит слово "кот" - выводит МЯУ,иначе - НЕТ
n = int(input('Введите кол-во предложений'))
mew = False
for i in range(1, n + 1):
    line = input()
    if 'Кот' in line or 'кот' in line:
        mew = True
if mew:
    print('МЯУ')
else:
    print('НЕТ')
