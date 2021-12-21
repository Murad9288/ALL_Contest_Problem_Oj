for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    i = n-1
    while i >= 0:
        if arr[i]%(i+2) != 0:
            arr.pop(i)
            i = len(arr)-1
        else:
            i -= 1
    if i<0 and len(arr) == 0:
        print("YES")
    else:
        print("NO")
