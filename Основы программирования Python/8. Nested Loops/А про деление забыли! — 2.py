# Отличие в том, что в данном случае вопроизводится деление на 1 в том числе
n_colonna = int(input())
n_line = int(input())
for i in range(1, n_line + 1):
    for j in range(1, n_colonna + 1):
        print(j / i, end=' ')
    print("")
