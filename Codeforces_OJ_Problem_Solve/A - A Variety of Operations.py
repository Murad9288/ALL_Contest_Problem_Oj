for _ in range(int(input())):
    a,b=map(int,input().split())
    if a==0 and b==0:
        print(0)
    elif a==b:
        print(1)
    elif (a+b)%2!=0 :
        print(-1)
    else:
        print(2)
