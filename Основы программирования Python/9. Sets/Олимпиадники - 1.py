# В школе проходит экзамен по немецкому и английскому языкам. Каждый ученик в школе
# сдаёт либо английский, либо немецкий, либо оба этих языка.
# У директора есть списки учеников и их фамилии изучающих каждый из языков.
# Вот только, к несчастью,списки учеников перемешались...

# Программа выводит, сколько учеников изучает только один язык.
english = int(input('Введите кол-во учеников, сдающих английский:'))
german = int(input('Введите кол-во учеников, сдающих немецкий:'))
crossing = set()
student_e_all = set()
student_g_all = set()
student_g = student_e = ''
print('Вводите фамилии учеников не в обязательном порядке:')
for i in range(english):
    student_e = input()
    if student_e in student_e_all:
        student_g_all.add(student_e)
    else:
        student_e_all.add(student_e)
for i in range(german):
    student_g = input()
    if student_g in student_g_all:
        student_e_all.add(student_g)
    else:
        student_g_all.add(student_g)
crossing = len(student_e_all ^ student_g_all)
if crossing == 0:
    print('Таких учеников нет')
else:
    print(crossing)