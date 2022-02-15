for _ in range(int(input())):
    s = str(input())
    a = s.count("M")
    b = s.count("P")
    c = s.count("C")
    if a>0 and b>0 and c>0:
        print("YES")
    else:
        print("NO")
