n = int(input())
announce = []
for i in range(n):
    part = input()
    announce.append(part)
n = int(input())
for i in range(n):
    part = int(input())
    print(announce[part - 1])
