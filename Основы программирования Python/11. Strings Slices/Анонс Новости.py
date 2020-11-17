# Программа сокращает броский заголовок газеты до указаной длины
preview = int(input('Введите длину:'))
n = int(input('Сколько будет заголовков? :'))
for i in range(n):
    head = input()
    if len(head) > preview:
        head = head[:preview - 3] + '...'
    print(head)
