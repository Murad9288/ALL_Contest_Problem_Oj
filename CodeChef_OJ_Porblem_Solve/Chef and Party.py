for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    c = 0
    for i in sorted(arr):
        if c>=i:
            c+=1
        else:
            break
    print(c)
