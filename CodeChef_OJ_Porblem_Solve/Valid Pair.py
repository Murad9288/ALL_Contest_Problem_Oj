try:
    a,b,c = map(int,input().split())
    if a==b or b == c or a == c and (a>=1 and b>=1 and c>=1 and a<11 and b<11 and c<11):
        print("YES")
    else:
        print("NO")
except:
    pass
