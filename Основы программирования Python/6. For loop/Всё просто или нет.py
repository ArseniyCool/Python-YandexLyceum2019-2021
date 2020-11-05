n = int(input('Введите целое число:'))
print('V Его делители представлены снизу V')
i = 1
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
        count += 1
    i += 1
if count > 2 or count == 1:
    print('\nЭто число СОСТАВНОЕ')
else:
    print('\nЭто число ПРОСТОЕ')
