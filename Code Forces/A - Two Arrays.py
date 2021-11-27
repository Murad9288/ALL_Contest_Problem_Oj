for _ in range(int(input())):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a.sort()
    b.sort()
    result = "YES"
    for i in range(n):
        if a[i]>b[i] or abs(a[i] - b[i])>1:
            result ="NO"
            break
    print(result)
