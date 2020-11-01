import random
# По игре Псевдоним c ботом, однако с 3 кучками
# Бот выбирает любую из кучек и берет рандомное количество камней из кучки
# Вы также можете брать любое корректное количество камней
bunch_1 = int(input('Введите изначальное количество камней в 1 кучке:'))
bunch_2 = int(input('Введите изначальное количество камней в 2 кучке:'))
bunch_3 = int(input('Введите изначальное количество камней в 3 кучке:'))
take_game = random.randint(1, 4)
count = 'bot'
end = 1
print('Ход:', count)
while end != 0:
    if count == 'bot' and 0 != (bunch_1 + bunch_2 + bunch_3) and end != 0:
        if 0 == bunch_1 and 0 == bunch_2:
            bunch = bunch_3
        elif 0 == bunch_1 and 0 == bunch_3:
            bunch = bunch_2
        elif 0 == bunch_2 and 0 == bunch_3:
            bunch = bunch_1
        elif 0 == bunch_1:
            bunch = random.choice([bunch_2, bunch_3])
        elif 0 == bunch_2:
            bunch = random.choice([bunch_1, bunch_3])
        elif 0 == bunch_3:
            bunch = random.choice([bunch_1, bunch_2])
        else:
            bunch = random.choice([bunch_1, bunch_2, bunch_3])
        if bunch == bunch_1:
            bunch_num = 1
        elif bunch == bunch_2:
            bunch_num = 2
        else:
            bunch_num = 3
        if 1 == bunch_1 or 1 == bunch_2 or 1 == bunch_3:
            take_bot = 1
        else:
            take_bot = random.choice(range(1, bunch))
            while take_bot > bunch_1 and take_bot > bunch_2 and take_bot > bunch_3:
                take_bot = random.choice(range(1, bunch))
        if bunch_num == 1:
            bunch_1 = bunch_1 - take_bot
        elif bunch_num == 2:
            bunch_2 = bunch_2 - take_bot
        else:
            bunch_3 = bunch_3 - take_bot
        print('Бот:', take_bot, 'из', bunch_num, 'кучки')
        print('==Осталось', bunch_1, bunch_2, bunch_3, 'камней==')
        count = 'player'
        print('Ход:', count)
    elif end != 0:
        print("Вы выиграли!")
        end = 0
    if count == 'player' and 0 != (bunch_1 + bunch_2 + bunch_3) and end != 0:
        n = int(input('Кучка:'))
        result1 = result2 = None
        while result1 != 'good' and result2 != 'good':
            if 1 == n or 2 == n or 3 == n:
                result1 = 'good'
            if (1 == n and 0 != bunch_1) or (2 == n and 0 != bunch_2):
                result2 = 'good'
            elif 3 == n and 0 != bunch_3:
                result2 = 'good'
            else:
                print("НЕ ОК")
                result1 = result2 = 'bad'
                n = int(input('Кучка:'))
        print("ОК")
        if n == 1:
            take = int(input())
            while take > bunch_1:
                print("НЕ ОК")
                take = int(input())
            bunch_1 = bunch_1 - take
            print("ОК")
            print('==Осталось', bunch_1, bunch_2, bunch_3, 'камней==')
            count = 'bot'
            print('Ход:', count)
        elif n == 2:
            take = int(input())
            while take > bunch_2:
                print("НЕ ОК")
                take = int(input())
            bunch_2 = bunch_2 - take
            print('==Осталось', bunch_1, bunch_2, bunch_3, 'камней==')
            count = 'bot'
            print('Ход:', count)
        else:
            take = int(input('Кол-во камней:'))
            while take > bunch_3:
                print("НЕ ОК")
                take = int(input('Кол-во камней:'))
            bunch_3 = bunch_3 - take
            print('==Осталось', bunch_1, bunch_2, bunch_3, 'камней==')
            count = 'bot'
            print('Ход:', count)
    elif end != 0:
        print("Вы проиграли...")
        end = 0
