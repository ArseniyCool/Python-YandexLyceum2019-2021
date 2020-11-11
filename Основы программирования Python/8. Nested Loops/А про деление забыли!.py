n_colonna = int(input())
n_line = int(input())
print("1", end='\t')
for i in range(2, n_colonna + 1):
    print(i, end='\t')
print("")
for i in range(2, n_line + 1):
    print(i, end=' ')
    for j in range(2, n_colonna + 1):
        print(j / i, end=' ')
    print("")
