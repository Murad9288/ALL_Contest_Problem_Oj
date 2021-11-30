n = int(input())
li = list(map(int,input().split())) [:n]
res = []
for i in range(0,len(li),2):
    res.append(li[i])
print(sum(res))
