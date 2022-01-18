for _ in range(int(input())):
    a,b=map(int,input().split())
    if a%b:
        print((b-a)%b)
    else:
        print(0)
