a,b,c=sorted(list(map(int,input().split())))
m = 0
for i in range(3):
    if a<i:
        break
    res = a - i + (c-a+i)//3 + (b-a+i)//3
    m = max(m,res)
print(m)
