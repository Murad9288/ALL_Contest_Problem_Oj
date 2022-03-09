for _ in range(int(input())):
    s = str(input())
    s2 = str(input())
    c = 0
    arr = []
    for i in s:
        c += 1
        if s2 == i:
            arr.append(c)
            c = 0
    res = 0
    print(arr)
    for j in arr:
        if j%2 != 0:
            res += 1
    if res>0:
        print("YES")
    else:
        print("NO")
