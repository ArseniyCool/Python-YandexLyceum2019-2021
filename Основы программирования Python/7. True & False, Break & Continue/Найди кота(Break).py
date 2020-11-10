# Программа считывает указанное число предложений,и если находит слово "кот" - преращает работу
# и выводит МЯУ,иначе - НЕТ
n = int(input('Введите кол-во предложений:'))
mew = False
for i in range(1, n + 1):
    line = input()
    if 'Кот' in line or 'кот' in line:
        mew = True
        break
if mew:
    print('МЯУ')
else:
    print('НЕТ')
