n = int(input())
c = []
if n % 2 == 0:
    for i in range(1,n,2):
        c.append(i)
    print(len(c))
    print(*c)
else:
    for j in range(1,n-1):
        c.append(j)
    print(len(c))
    print(*c)
