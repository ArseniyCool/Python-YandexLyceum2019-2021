import random
# По задаче Псевдоним (с одной кучей, можно взять до трёх камней) c ботом.
# но взявший последний камень не выигрывает, а проигрывает.
all_stones = int(input('Введите изначальное количество камней в кучке:'))
take_game = random.randint(1, 3)
while all_stones != -1:
    if 0 != all_stones:
        take_game = random.choice([1, 2, 3])
        while take_game > all_stones:
            take_game = random.choice([1, 2, 3])
        all_stones = all_stones - take_game
        print('Бот:', take_game)
        print('Осталось', all_stones, 'камней')
        # Если введено некорректное количество камней,
        # то программа запрашивает выбрать камни повторно
        if 0 != all_stones:
            take = int(input('Введите кол-во камней:'))
            while 3 < take or take == 0 or take > all_stones:
                take = int(input('Введите кол-во камней:'))
            all_stones = all_stones - take
            print('Осталось', all_stones, 'камней')
        else:
            print("Вы выйграли!")
            all_stones -= 1
    else:
        print("Вы проиграли...")
        all_stones -= 1
