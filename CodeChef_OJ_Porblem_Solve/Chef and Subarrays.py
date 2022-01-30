try:
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))[:n]
        c = 0
        for i in range(0,n):
            s = 0
            m = 1
            for j in range(i,n):
                m *= arr[j]
                s += arr[j]
                if s == m:
                    c += 1
        print(c)

except:
    pass
