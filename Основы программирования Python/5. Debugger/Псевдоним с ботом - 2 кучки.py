# По игре Псевдоним c ботом, однако с 2 кучками
# Бот выбирает любую из кучек и берет рандомное количество камней из кучки
# Вы также можете брать любое корректное количество камней
import random
bunch_1 = int(input('Введите изначальное количество камней в 1 кучке:'))
bunch_2 = int(input('Введите изначальное количество камней в 2 кучке:'))
take_game = random.randint(1, 3)
count = 'bot'
end = 1
print('Вводите поочерёдно сначала номер кучки, затем кол-во камней (во время Вашего хода)')
print()
print('Ход:', count)
while end != 0:
    if count == 'bot' and 0 != (bunch_1 + bunch_2) and end != 0:
        if 0 == bunch_1:
            bunch = bunch_2
            bunch_num = 2
        elif 0 == bunch_2:
            bunch = bunch_1
            bunch_num = 1
        else:
            bunch = random.choice([bunch_1, bunch_2])
            if bunch == bunch_1:
                bunch_num = 1
            else:
                bunch_num = 2
        if 1 == bunch_1 or 1 == bunch_2:
            take_bot = 1
        else:
            take_bot = random.choice(range(1, bunch))
            while take_bot > bunch_1 and take_bot > bunch_2:
                take_bot = random.choice(range(1, bunch))
        if bunch_num == 1:
            bunch_1 = bunch_1 - take_bot
        else:
            bunch_2 = bunch_2 - take_bot
        print('Бот:', take_bot, 'из', bunch_num, 'кучки')
        print('Осталось', bunch_1, bunch_2, 'камней')
        count = 'player'
        print('Ход:', count)
    elif end != 0:
        print("Вы выиграли!")
        end = 0
    if count == 'player' and 0 != (bunch_1 + bunch_2) and end != 0:
        n = int(input('Кучка:'))
        while (1 != n and 2 != n) or (1 == n and 0 == bunch_1) or (2 == n and 0 == bunch_2):
            print("НЕ ОК")
            n = int(input('Кучка:'))
        print("ОК")
        if n == 1:
            take = int(input('Кол-во камней:'))
            while take > bunch_1:
                print("НЕ ОК")
                take = int(input('Кол-во камней:'))
            bunch_1 = bunch_1 - take
            print("ОК")
            print('Осталось', bunch_1, bunch_2, 'камней')
            count = 'bot'
            print('Ход:', count)
        elif n == 2:
            take = int(input('Кол-во камней:'))
            while take > bunch_2:
                print("НЕ ОК")
                take = int(input('Кол-во камней:'))
            bunch_2 = bunch_2 - take
            print(bunch_1, bunch_2)
            count = 'bot'
            print('Ход:', count)
    elif end != 0:
        print("Вы проиграли...")
        end = 0
