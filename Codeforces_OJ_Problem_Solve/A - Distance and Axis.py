for _ in range(int(input())):
    a,b = map(int,input().split())
    if a <= b:
        print(b-a)
    else:
        if (a+b)%2 == 0:
            print(0)
        else:
            print(1)


