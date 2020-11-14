# В школе проходит экзамен по немецкому и английскому языкам. Каждый ученик в школе
# сдаёт либо английский, либо немецкий, либо оба этих языка.
# У директора есть списки учеников и их фамилии изучающих каждый из языков.

# Программа выводит, сколько учеников изучает только один язык.
english = int(input('Введите кол-во учеников, сдающих английский:'))
german = int(input('Введите кол-во учеников, сдающих немецкий:'))
crossing = set()
student_e = set()
student_g = set()
print('Вводите фамилии учеников по порядку:')
for i in range(english):
    student_e.add(input())
for i in range(german):
    student_g.add(input())
crossing = len(student_e ^ student_g)
if crossing == 0:
    print('Таких учеников нет')
else:
    print(crossing)
