# Contest Code:DEC21C
# Problem Code:UTKPLC
# 1000% Accepted:

try:
    for _ in range(int(input())):
        f,s,t = map(str,input().split())
        x,y = map(str,input().split())
        if (x == f and y == s) or (x == f and y == t) or (x == s and y == t):
            print(x)
        else:
            print(y)
except:
    pass
