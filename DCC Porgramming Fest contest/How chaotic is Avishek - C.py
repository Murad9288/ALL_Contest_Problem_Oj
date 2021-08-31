for T in range(int(input())):
    N,H,K,X = map(int,input().split())
    r = K//N
    c = 0
    if r/H > X:
        print("%d YES"%(r))
    else:
        print("%d NO"%(r))
