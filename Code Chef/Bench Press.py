# First Rules:
# Contest Code:PRACTICE (Problem Code:BENCHP)
try:
    for _ in range(int(input())):
        n,w,r=map(int,input().split())
        li=list(map(int,input().split()))
        li.sort()
        c = 1
        result = 0
        for i in range(n-1):
            if (li[i] == li[i+1]):
                c += 1
            else:
                result = result + (2*(c//2)*(li[i]))
                c=1
        result = result + (2*(c//2)*(li[n-1])) + r
        if(result>=w):
            print("YES")
        else:
            print("NO")
except:
    pass

# Second rules:
'''
try:
    for _ in range(int(input())):
        n,w,r = map(int,input().split())
        L = list(map(int,input().split()))
        m = w-r
        res = False
        if m<=0:
            print("YES")
            continue
        c = dict()
        for i in range(n):
            c[L[i]] = c.get(L[i],0) + 1
        for j,v in c.items():
            if v>=2:
                if v%2!=0:
                    v -= 1
                m -= v*j
            if m<=0:
                res = True
        if res:
            print("Yes")
        else:
            print("No")
except:
    pass

'''
