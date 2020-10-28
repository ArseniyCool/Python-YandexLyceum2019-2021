# На профессию космонавта принимаются только люди ростом от 150 до 190 сантиметров
# Программа считывает сколько добровольцев из данных годятся в космонавты,а также
# Минимальный и максимальный рост участников
test = input()
count = 0
test_min = 190
test_max = 150
while test != "!":
    test = int(test)
    # Cигнал остановки - !
    if 150 <= test <= 190:
        count += 1
        if test_min > test:
            test_min = test
        if test_max < test:
            test_max = test
    test = input()
print(count)
print(test_min, test_max)
