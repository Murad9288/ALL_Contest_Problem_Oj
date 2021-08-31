import math
T = int(input())
for i in range(T):
        
        n = int(input())
        count = 0
        for i in range(1,n+1):
                
                 s = int(math.sqrt(i))
                 if s*s ==i:
                         a = s**2
                         count += 1
                         print(a,end=",")
        print("\n",count)
