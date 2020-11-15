word = input('Слово:-')
num = int(input('Номер буквы? :'))
if 0 < num <= len(word):
    print(word[num - 1])
else:
    print('ОШИБКА')
