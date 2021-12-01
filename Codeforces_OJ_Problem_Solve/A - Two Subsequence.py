for _ in range(int(input())):
    s = str(input())
    m = min(s)
    n = s.replace(m,"",1)
    print(m,n)
