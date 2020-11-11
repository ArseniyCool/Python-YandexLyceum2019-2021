# Программа выводит простые числа в пределе max_val
max_val = int(input("Кол-во чисел,по которым строится столб простых чисел:"))
counter = 2
while counter < max_val:
    is_prime = True
    if 0 == counter % 2 and counter != 2:
        is_prime = False
    for i in range(3, int(counter / 2), 2):
        if 0 == counter % i or not is_prime:
            is_prime = False
            break
    if is_prime:
        print(counter)
    counter += 1
