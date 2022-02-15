for _ in range(int(input())):
    n = int(input())
    st = "10"
    if n%2==0:
        print(int(n/2)*st)
    else:
        print(-1)
