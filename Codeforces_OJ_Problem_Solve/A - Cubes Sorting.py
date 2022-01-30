for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    for i in range(1,n):
        if arr[i]>=arr[i-1]:
            print("YES")
            break
    else:
        print("NO")
