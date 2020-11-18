# Программа проверяет наличие неразрешённых символов в имени пользователя
alphabet = set()
for i in range(26):
    # Английские заглавные буквы
    alphabet.add(chr(ord('A') + i))
    # Английские строчные буквы
    alphabet.add(chr(ord('a') + i))
    if i <= 10:
        # Цифры
        alphabet.add(chr(ord('0') + i))
# Знак "_"
alphabet.add('_')
name = input('')
symbol = True
for i in range(0, len(name)):
    if name[i] not in alphabet:
        if name[i] == ' ':
            print('Неверный символ:', 'Пробел')
        else:
            print('Неверный символ:', name[i])
        symbol = False
        break
    symbol = True
if symbol:
    print('OK')
