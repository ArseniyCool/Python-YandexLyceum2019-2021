# Вы Начальник кадровой службы, который хочет узнать, сколько однофамильцев работает в организации.
# У него есть список фамилий, и на основании этого списка нужно вычислить количество фамилий,
# которые совпадают с другими.
N = int(input('Кол-во сотрудников'))
namesake = set()
not_namesake = set()
count = 0
# Вводите поочередно фамилии
for i in range(N):
    surname = input()
    if surname not in not_namesake:
        not_namesake.add(surname)
    elif surname not in namesake:
        namesake.add(surname)
    else:
        count += 1
count += 2 * len(namesake & not_namesake)
print(count)
