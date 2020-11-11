# Ширина таблицы Улама
n = int(input())
# Кол-во чисел,о которым строится таблица
max_val = int(input())
counter = 1
while counter <= max_val:
    is_prime = True
    if 0 == counter % 2 and counter != 2:
        is_prime = False
    for y in range(3, int(counter / 2), 2):
        if 0 == counter % y or not is_prime:
            is_prime = False
            break
    if is_prime:
        print('#', end="\t")
    else:
        print(".", end="\t")
    counter += 1
    if 0 == counter % n:
        print("")
