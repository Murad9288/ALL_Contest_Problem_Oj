n = int(input())
c = 0
li = []
for i in range(n):
    li.append(input().upper())
for i in li:
    if '++' in i:
        c += 1
    else:
        c -= 1
print(c)
