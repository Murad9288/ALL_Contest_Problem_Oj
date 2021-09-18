T = int(input())
for i in range(1,T+1):
    a,b = map(int,input().split())
    count = []
    for j in range(a,b):
        if j > 0:
            for k in range(2,j):
                if j%k == 0:
                    break
            else:
                count.append(j)
    print(len(count))

 

