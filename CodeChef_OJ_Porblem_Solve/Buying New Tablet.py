for _ in range(int(input())):
    N,B = map(int,input().split())
    cnt = 0
    for _ in range(N):
       a,b,c = map(int,input().split())
       if c<=B:
           cnt = max(cnt,a*b)
    if cnt == 0:
        print("no tablet")
    else:
        print(cnt)
