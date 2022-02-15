for _ in range(int(input())):
    a = sorted(str(input()))
    h = str(input())
    for i in range(len(h) - len(a) + 1):
        if sorted(h[i:i + len(a)]) == a:
            print("YES")
            break
    else:
        print("NO")
