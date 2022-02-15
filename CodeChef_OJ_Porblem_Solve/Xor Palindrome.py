for _ in range(int(input())):
    n = int(input())
    s = str(input())
    z = 0
    o = 0
    for i in range(n):
        if s[i] == "0":
            z += 1
        else:
            o += 1
    if n%2 == 0:
        if z%2 == 0 and o%2 == 0 or z == o:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")
