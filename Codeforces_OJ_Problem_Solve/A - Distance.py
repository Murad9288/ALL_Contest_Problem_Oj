for _ in range(int(input())):
    x,y = list(map(int,input().split()))
    if x%2 == 0 and y%2 == 1:
        print(-1,-1)
    elif x%2 == 1 and y%2 == 0:
        print(-1,-1)
    else:
        if x%2 == 0:
            print(x//2,y//2)
        elif x%2 == 1:
            print((x-1)//2,(y+1)//2)
