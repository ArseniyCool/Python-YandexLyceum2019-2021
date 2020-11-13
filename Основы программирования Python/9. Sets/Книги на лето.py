# Представьте, что Вам задали читать книги на лето
# К счастью, у Вас на компьютере есть текстовый документ, в котором записаны
# все книги из его домашней библиотеки в случайном порядке.

# Программа определяет, какие книги из списка на лето у Вас есть, а каких нет.
M = int(input('Введите кол-во книг на Вашем компьютере:'))
N = int(input('Введите кол-во книг на лето:'))
library = set()
# Вводите названия книг согласно их количеству
for i in range(M):
    book = input()
    library.add(book)
for i in range(N):
    spisok = set()
    book = input()
    spisok.add(book)
    if spisok <= library:
        print('Есть')
    else:
        print('Нет')
