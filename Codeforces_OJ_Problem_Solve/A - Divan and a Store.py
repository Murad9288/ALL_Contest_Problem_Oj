for _ in range(int(input())):
    n,l,r,k=[int(i) for i in input().split()]
    arr=list(map(int,input().split()))
    arr=[x for x in arr if (x>=l and x<=r)]
    arr.sort()
    x=0
    y=0
    if(sum(arr)<=k):
        print(len(arr))
    else:
        for j in arr:
            x+=j
            y+=1
            if(x>k):
                x-=j
                y-=1
                break
        print(y)
