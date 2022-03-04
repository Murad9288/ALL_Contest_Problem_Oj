for _ in range(int(input())):
    n = int(input())
    arr = [2,3,1]
    if n == 2:
        print(-1)
    elif n%2 != 0:
        arr2 = []
        for i in range(n,0,-1):
            arr2.append(i)
        print(*arr2)
    elif n == 4:
        print(3,2,4,1)
    else:
        for i in range(4,n+1):
            arr.append(i)
        print(*arr)
