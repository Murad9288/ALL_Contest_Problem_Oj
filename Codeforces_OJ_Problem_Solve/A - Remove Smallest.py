for _ in range(int(input())):
    c = 0
    n = int(input())
    arr = sorted(set(map(int, input().split())))
    if (arr[len(arr)-1]) - arr[0] == (len(arr)-1):
        c = 1
    if c != 0:
        print("YES")
    else:
        print("NO")
