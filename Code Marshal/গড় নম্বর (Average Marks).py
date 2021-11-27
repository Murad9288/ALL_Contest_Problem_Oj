for i in range(int(input())):
     li = list(map(int,input().split()))
     n = li[0]
     s = li[1:]
     print("Case %d: %d"%(i+1,sum(s)//n))
