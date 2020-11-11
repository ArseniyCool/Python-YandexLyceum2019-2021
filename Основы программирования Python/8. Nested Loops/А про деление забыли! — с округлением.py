# Отличие в том, что в данном случае вопроизводится деление c округлением до сотой части
n_colonna = int(input())
n_line = int(input())
print("1", end='     ')
for i in range(2, n_colonna + 1):
    print(i, end='     ')
print("")
for i in range(2, n_line + 1):
    print(i, end='   ')
    for j in range(2, n_colonna + 1):
        print(round(j / i, 2), end='   ')
    print("")
