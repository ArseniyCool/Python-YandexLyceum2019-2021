print('"Здорова,сталкер!Куда путь держишь?"')
a = input('(1 - К Сидоровичу, продать барахло;2 На свалку за артефактами;3 К монолиту):')
if a == '1':
    print('Вы отправились к Сидоровичу на Кордон.По дороге Вы вновь перестреляли военных,')
    print('вечно сидящих вблизи моста и наконец дошли до лагеря новичков')
    print('При встрече с Сидоровичем он вам и ответил:')
    print('"Ты бы еще консервных банок насобирал,Меченый!')
elif a == '2':
    print('Вы отправились на свалку искать подарки ученым.')
    print('Собрали артефактов сполна,пора выбираться - вот только выброс и не думал ждать.')
    print('Так и остался ваш труп отдыхать,в бедствии - висеть на дереве впоследствие,')
    print('показывая сталкерам,что существуют дураки,идущие на аномальную свалку без брони...')
elif a == '3':
    print('Вы побрели к центру Зоны, ни капли не волнуясь идти туда с единой аптечкой с Пмм...')
    print('На удивленье,вы добрались до Монолита.Какое желание загадаете?')
    d = input('(1 - Хочу богатство!; 2 - Хочу домой!)')
    if d == '1':
        print('[Оригинальная концовка STALKER:ТЧ]')
    elif d == '2':
        print('За эти умопомрачительно-ужасные годы на Зоне,которые вы провели,')
        print('ад действительно стал вашим домом...Монолит исполнил ваше желание!')
        print('Добро пожаловать!')
    else:
        print('Иди своей дорогой,Псевдосталкер!(Ошибка 404!)')
else:
    print('Иди своей дорогой,Псевдосталкер!(Ошибка 404!)')
