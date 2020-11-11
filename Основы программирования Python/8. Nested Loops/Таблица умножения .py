n = int(input())
print("1", end='\t')
for i in range(2, n + 1):
    print(i, end='\t')
print("")
for i in range(2, n + 1):
    print(i, end='\t')
    for j in range(2, n + 1):
        print(i * j, end='\t')
    print("")
