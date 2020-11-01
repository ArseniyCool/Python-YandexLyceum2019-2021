import random
# По игре Псевдоним-пасьянс (С теми же ограничениями),
# но с ботом, который берет рандомное количество камней из кучки
all_stones = int(input('Введите изначальное количество камней в кучке:'))
take_game = random.randint(1, 3)
print('Вводите поочерёдно кол-во камней,которое Вы хотите забрать из кучки:')
while all_stones != -1:
    if 0 != all_stones:
        take_game = random.choice([1, 2, 3])
        while take_game > all_stones:
            take_game = random.choice([1, 2, 3])
        all_stones = all_stones - take_game
        print('Бот:', take_game)
        print('Осталось', all_stones, 'камней')
        if 0 != all_stones:
            take = int(input('Вы:'))
            while 3 < take or take == 0 or take > all_stones:
                take = int(input())
            all_stones = all_stones - take
            print(all_stones)
        else:
            print("Вы проиграли...")
            all_stones -= 1
    else:
        print("Вы выйграли!")
        all_stones -= 1
