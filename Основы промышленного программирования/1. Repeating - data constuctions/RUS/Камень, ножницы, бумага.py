choice_1 = input()
choice_2 = input()
result = ''
if choice_1 == 'ножницы':
    if choice_2 == 'бумага':
        result = 'первый'
    elif choice_2 == 'камень':
        result = 'второй'
    else:
        result = 'ничья'
elif choice_1 == 'бумага':
    if choice_2 == 'камень':
        result = 'первый'
    elif choice_2 == 'ножницы':
        result = 'второй'
    else:
        result = 'ничья'
else:
    if choice_2 == 'ножницы':
        result = 'первый'
    elif choice_2 == 'бумага':
        result = 'второй'
    else:
        result = 'ничья'
print(result)
