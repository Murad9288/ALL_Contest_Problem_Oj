for _ in range(int(input())):
    n = int(input())
    arr = sorted(list(map(int,input().split()))[:n])
    while arr:
        print(arr.pop(len(arr)//2),end=" ")
    print()

