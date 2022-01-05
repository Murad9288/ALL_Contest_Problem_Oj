a,b,c,d = sorted(list(map(int,input().split())))
if c<a+b or d<b+c or d<a+c or d<a+b:
    print("TRIANGLE")
elif a+b == c or b+c == d or a+c == d or a+b == d:
    print("SEGMENT")
else:
    print("IMPOSSIBLE")
