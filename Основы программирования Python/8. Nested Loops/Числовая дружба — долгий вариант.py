import math
# Второй вариант "Числовой дружбы"
# Два натуральных числа называются дружественными, если каждое из них равно
# сумме всех делителей другого (само другое число в качестве делителя не рассматривается).
# Например, 220 (1+2+4+5+10+11+20+22+44+55+110=284) и 284 (1+2+4+71+142=220) – дружественные числа.

# Программа находит пары натуральных дружественных чисел, меньших 10 000.
counter = 2
prime_nums = set()
while counter < 10000:
    is_prime = True
    if 0 == counter % 2 and counter != 2:
        is_prime = False
    for i in range(3, int(math.sqrt(counter)), 2):
        if 0 == counter % i or not is_prime:
            is_prime = False
            break
    if is_prime:
        prime_nums.add(counter)
    counter += 1
z = set()
for i in range(3, 10000):
    z.add(i)
z -= prime_nums
for i in z:
    a = 0
    b = 0
    for j in range(1, i):
        if i % j == 0:
            a += j
    for y in range(1, a):
        if a % y == 0:
            b += y
    if i > a:
        if i == b and i != a and i == a:
            print(i, a)
    else:
        if i == b and i != a:
            print(i, a)
