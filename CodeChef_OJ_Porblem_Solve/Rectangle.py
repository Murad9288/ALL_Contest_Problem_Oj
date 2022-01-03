try:
    for _ in range(int(input())):
        a,b,c,d = map(int,input().split())
        arr = sorted([a,b,c,d])
        if arr[0] == arr[1] and arr[2] == arr[3]:
            print("YES")
        else:
            print("NO")
except:
    pass




