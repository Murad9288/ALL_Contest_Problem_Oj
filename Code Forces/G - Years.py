x = []
for _ in range(int(input())):
    a,b = map(int,input().split())
    x.append([a,1])
    x.append([b,-1])
x.sort()
y = []
max = -1
cur = 0
for i in range(len(x)):
    cur += x[i][1]
    if(cur>max):
        max = cur
        y = x[i][0]

print(y,max)
