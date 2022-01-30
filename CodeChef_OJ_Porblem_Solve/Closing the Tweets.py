# cook your dish here
n,k = map(int,input().split()) 
c = [0]*n
for i in range(0,k):
    s = input()
    if (s == "CLOSEALL"):
        for j in range(0,n):
            c[j] = 0
    
    else:
      s = s.replace('CLICK ','')
      c[int(s)-1] += 1

    o = 0
    for i in c:
        if(i%2 != 0):
            o += 1
    print(o)
