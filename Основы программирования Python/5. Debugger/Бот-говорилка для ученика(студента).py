text = "Бот-говорилка"
while not('пока' in text) or not('до свидания' in text):
    text = input('Привет,я бот-говорилка.Сколько со мной собираешься общаться?')
    if ('много' in text) or ('долго' in text) or ('день' in text):
        text = input('Круто!Я доволен! О чем поговорим?')
    elif ('чуть-чуть' in text) or ('мало' in text):
        text = input('Печально,надеюсь у тебя хоть минутка найдется!О чем поговорим?')
    if ('уроки' in text) or ('школа' in text) or ('дз' in text):
        print('Хахха,давай,рассказывай свой секрет!')
        text = input('Какую оценку сегодня получил по алгебре?')
        if ('двойка' in text) or ('2' in text):
            print('Так и знал! Вангую,ночевать в школе/универе придется - домой не пустят! :S')
        elif ('тройка' in text) or ('3' in text):
            print('Оу,ну это победа! Уже накрываю на стол,сегодня праздник! :D')
        elif ('четверка' in text) or ('4' in text):
            print('А я пулю зубами сегодня словил!')
            print('Ровно так я тебе поверил! :>')
        elif ('пятерка' in text) or ('5' in text):
            print('Твоя мечта сбылась,теперь можно вернуться домой с достоинством :l')
    elif ('отдых' in text) or ('свобода' in text) or ('устал' in text):
        print('Понимаю тебя!В школе/универе и в правду сложно учиться....')
        text = input('Давай я расскажу 1 из 3 способов расслабиться.Какой хочешь услышать?')
        if ('первый' in text) or ('1' in text):
            text = input('Я узнал,что завтра экзамен/сессия по физике.Ну как,расслабился?')
            if 'да' in text:
                print('Cерьезно? Кто ты такой!')
            elif 'нет' in text:
                print("Уверен,теперь ты не уснешь этой ночью...")
            else:
                print('Извини,я тебя не понимаю,ну да ладно!Давай заново поговорим!')
        elif ('второй' in text) or ('2' in text):
            print('Два..Два...Два...Чувствуешь? Она повсюду тебя окружает. Но тебя не должно это')
            print('волновать...Ведь когда-нибудь ты и получишь пять...НЕТ, этого не случится! Ахаха')

        elif ('третий' in text) or ('3' in text):
            print('Сделай глубокий вдох...И выдох...Ляг на кровать,зажмурь глаза,усни ')
            print('И забудь об огромной стопке уроков,которые тебе нужно сделать на завтра ')
    elif ('яндекс.лицей' in text) or ('python' in text) or ('питон' in text):
        print('Ну давай...Ты знал,что сейчас на самом деле ты говоришь с Python ботом,')
        print('которого ты вчера создал? ДА,МЫ ВСЕ ЖИВЕМ В МАТРИЦЕ,ВСЕ МЫ БОТЫ')
        print('И ПОМНИ,РЕАЛЬНОСТЬ ИЛЛЮЗИЯ,ВСЕЛЕННАЯ ГОЛОГРАММА,СКУПАЙТЕ ЗОЛОТО...[Глюк программы]')
    elif ('пока' in text) or ('до свидания' in text):
        print('Уже уходишь? Пока...(Ты не уйдешь отсюда)')
    print('Давай заново поговорим!')
