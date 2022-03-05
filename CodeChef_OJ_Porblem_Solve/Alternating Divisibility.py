for _ in range(int(input())):
    n = int(input())
    a = [0]*n
    if n == 1:
        print(1)
        continue
    c = 1
    for i in range(0,n-1,2):
        a[i] = c
        a[i+1] = c*2
        c += 2
    if n%2 != 0:
        a[n-1] = a[n-2]+1
    print(*a)
