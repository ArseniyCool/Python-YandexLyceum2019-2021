# По игре Ним-пасьянс, однако с 2-мя кучками
# Гарантируется, что суммарное количество взятых им камней равно общему количеству камней в куче.
stack_1 = int(input('Введите изначальное количество камней в 1 кучке:'))
stack_2 = int(input('Введите изначальное количество камней в 2 кучке:'))
print('Вводите поочерёдно сначала номер кучки, затем кол-во камней,которое Вы хотите забрать:')
while stack_1 != 0 or stack_2 != 0:
    number = int(input())
    amount = int(input())
    if number == 1:
        stack_1 -= amount
    else:
        stack_2 -= amount
        # если Вы взяли номер группы больше чем 2, автоматически берутся камни
        # из 2 кучки
    print('Осталось 1)', stack_1, '2)', stack_2, 'камней')
