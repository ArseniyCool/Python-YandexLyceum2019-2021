i = 1
f = 1
for i in range(1, int(input())):
    print(f, end=' => ')
    f = f * (i + 1)
    i += 1
print(f)
