import math
for i in range(int(input())):
    a,b,r,c,d = map(int,input().split())
    res = math.sqrt(pow((a-c),2) + pow((b-d),2))
    if res<r:
        print("Case %d: yes"%(i+1))
    else:
        print("Case %d: no"%(i+1))
