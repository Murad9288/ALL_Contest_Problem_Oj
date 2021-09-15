# Problem = 5:
# Problem name: Positive Sweping.
try:
    for _ in range(int(input())):
        n,s=map(int,input().split())
        l=list(map(int,input().split()))
        e=l.copy()
        if any(l)>0:
            q=0
            for i in range(s):
                q+=1
                for j in range(len(l)):
                    if l[j]>0:
                        if j+1<n:
                            e[j+1]+=1
                        else:
                            e[0]+=1
                        if j-1>=0:
                            e[j-1]+=1
                        else:
                            e[n-1]+=1
                l=e.copy()
                if all(e)>0:
                    break
            ans=sum(e)+n*(s-q)*2
            print(ans)
        else:
            print(0)
except:
    pass
