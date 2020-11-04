height = int(input())
i = 1
a = "_"
x = " "
for i in range(1, height + 1):
    print(x * i, end='')
    print(a * i, end='\n')
    i += 1
