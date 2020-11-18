# Программа проверяет наличие неразрешённых символов в имени пользователя
alphabet = set()
for i in range(32):
    # Русские заглавные буквы
    alphabet.add(chr(ord('А') + i))
    # Русские строчные буквы
    alphabet.add(chr(ord('а') + i))
    if i <= 10:
        # Цифры
        alphabet.add(chr(ord('0') + i))
# Знак "_"
alphabet.add('_')
print('Разрешённые символы:')
print(alphabet)
name = input('Введите имя пользователя:')
symbol = True
for i in range(0, len(name)):
    if name[i] not in alphabet:
        print('---', name[i])
        if name[i] == ' ':
            print('Неверный символ:', 'Пробел')
        else:
            print('Неверный символ:', name[i])
        symbol = False
        break
    symbol = True
if symbol:
    print('OK')
