height = int(input())
i = 1
a = "M"
x = " "
count = 0
width = height - 1
for i in range(1, height + 1):
    print(x * width, end='')
    if i == 1:
        print(a * i, end='\n')
    else:
        count += 1
        print(a * (i + count), end='\n')
    i += 1
    width -= 1
