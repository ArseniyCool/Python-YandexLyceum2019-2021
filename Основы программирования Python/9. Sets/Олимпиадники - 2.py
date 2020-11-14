# В школе проходит экзамен по немецкому,английскому и французскому языкам.
# Каждый ученик в школе сдаёт либую возможную комбинацию этих языков.
# У директора есть списки учеников и их фамилии изучающих каждый из языков.
# Вот только, к несчастью,списки учеников перемешались...

# Программа выводит, сколько учеников изучает именно два языка.
english = int(input('Введите кол-во учеников, сдающих английский:'))
german = int(input('Введите кол-во учеников, сдающих немецкий:'))
french = int(input('Введите кол-во учеников, сдающих французский:'))
crossing = set()
std_e_all = set()
std_g_all = set()
std_f_all = set()
student_g = student_e = student_f = ''
print('Вводите фамилии учеников не в обязательном порядке:')
for i in range(english):
    student_e = input()
    if student_e in std_e_all:
        std_g_all.add(student_e)
    elif student_e in std_g_all:
        std_f_all.add(student_e)
    else:
        std_e_all.add(student_e)
for i in range(german):
    student_g = input()
    if student_g in std_g_all:
        if student_g in std_e_all and len(std_e_all) != english:
            std_f_all.add(student_g)
        else:
            std_e_all.add(student_g)
    else:
        std_g_all.add(student_g)
for i in range(french):
    student_f = input()
    if student_f in std_f_all:
        if student_f in std_e_all and len(std_e_all) != english:
            std_g_all.add(student_f)
        else:
            std_e_all.add(student_f)
    else:
        std_f_all.add(student_f)
student_union = std_e_all & std_g_all & std_f_all
if len(student_union) != 0:
    std_e_all -= student_union
    std_g_all -= student_union
    std_f_all -= student_union
crossing = len(std_e_all & std_g_all) + len(std_e_all & std_f_all) + len(std_g_all & std_f_all)
if crossing == 0:
    print('Таких учеников нет')
else:
    print(crossing)
