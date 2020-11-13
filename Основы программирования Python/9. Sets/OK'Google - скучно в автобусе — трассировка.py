# Игра:
#  Вы едете на автобусе и, чтобы развеять скуку, придумали себе игру.
#  Вы смотрите в окно и записывает все номера домов на тетрадный листок.
#  На середине пути Вы решаете взять новый листок и продолжаете записывать номера.

# Программа выводит, какие номера встретились и в первом, и во втором листочке
first_list = set()
second_list = set()
third_list = set()
for i in range(2):
    print('---', i)
    paper = input('')
    while paper != '':
        if i == 1:
            first_list.add(paper)
        else:
            second_list.add(paper)
        print('---', first_list)
        print('---', second_list)
        paper = input('')
third_list = first_list.intersection(second_list)
print('---', third_list)
if third_list == set():
    print('Таких нет')
else:
    for elem in third_list:
        print(elem)
