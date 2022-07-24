a = [0]*1000001
b = [0]*1000001
d = [0]*1000001
m = 998244353

def f_1(x,y):
    if x<0 or y>x:
        return 0
    return a[x]*d[y]%m*d[x-y]%m

a[0] = b[0] = b[1] = d[0] = d[1] = 1
for i in range(1,1000001):
    a[i] = a[i-1]*i%m
for i in range(2,1000001):
    b[i] = m-m//i*b[m%i]%m
for i in range(2,1000001):
    d[i] = d[i-1]*b[i]%m
    
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    c = c1 = r = 0
    for i in range(n):
        if arr[i] == 0:
            c += 1
        else:
            c1 += 1
    for i in range(c1+1):
        r = (r+i*f_1(c1+c-i,c))%m
    print((((r*(c+1)-f_1(c1+c-2,c-1))%m+m)%m+f_1(c1+c-2,c-1))*a[c1]%m*a[c]%m)
