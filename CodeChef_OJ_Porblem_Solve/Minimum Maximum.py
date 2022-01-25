for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(min(arr) * (len(arr)-1))
