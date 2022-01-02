for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    if sum(arr)%2 != 0:
        print("YES")
    else:
        for i in range(n):
            arr[i] = arr[i]%2
        if arr.count(1) > 0 and arr.count(0) > 0:
            print("YES")
        else:
            print("NO")
