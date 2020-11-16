# Сначала выбирается шаг шифрования (число),
# а затем все буквы послания заменяются на буквы, отстоящие от них в алфавите на шаг шифрования.
# Например, при шаге шифрования 3 (таким чаще всего пользовался Цезарь),
# буква А заменяется на букву Г, буква Б – на букву Д.
# При чем алфавит «зациклен», то есть при сдвиге буквы Я на шаг 3 получится буква В.

# Программа зашифровывает послание с помощью шифра Цезаря с заданным шагом шифрования.
n = int(input('Введите ключ шифра:'))
sense = input('Введите предожение:')
alphabet_1 = set()
alphabet_2 = set()
# Cоздание алфавита
for i in range(32):
    # Русские заглавные буквы
    alphabet_1.add(chr(ord('А') + i))
    # Русские строчные буквы
    alphabet_2.add(chr(ord('а') + i))
# Шифровка
for i in range(len(sense)):
    letter = sense[i]
    if letter in alphabet_1:
        if ord(letter) + n > ord('Я'):
            sense_2 = (chr((ord(letter) + n + 1) - 33))
        elif ord(letter) + n == ord('Я'):
            sense_2 = 'Я'
        else:
            sense_2 = (chr(ord(letter) + n))
    elif letter in alphabet_2:
        if ord(letter) + n > ord('я'):
            sense_2 = (chr((ord(letter) + n + 1) - 33))
        elif ord(letter) + n == ord('я'):
            sense_2 = 'я'
        else:
            sense_2 = (chr(ord(letter) + n))
    else:
        sense_2 = letter
    print(sense_2, end='')
