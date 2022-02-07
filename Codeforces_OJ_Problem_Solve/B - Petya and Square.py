n,x,y = map(int,input().split())
n = n//2
if n<=x<=n+1 and n<=y<=n+1:
    print("NO")
else:
    print("YES")
