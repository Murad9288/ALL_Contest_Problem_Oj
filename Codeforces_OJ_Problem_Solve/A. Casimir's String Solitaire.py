for _ in range(int(input())):
    s = str(input())
    a = s.count("A")
    b = s.count("B")
    c = s.count("C")
    if b == a+c:
        print("YES")
    else:
        print("NO")
