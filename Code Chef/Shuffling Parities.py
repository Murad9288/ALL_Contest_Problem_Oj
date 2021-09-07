# First Rules:
try:
    for _ in range(int(input())):
            n = int(input())
            odd =0
            even=0
            a = list(map(int, input().split( )))
            for i in a:
                if i%2==1:
                    odd+=1
                else:
                    even+=1
            result = min(even, (n+1)//2 ) + min(odd, n//2)
            print(result)
except:
    pass
# Second Rules:
'''

import math
try:
    for _ in range(int(input())):
        n = int(input())
        li = list(map(int,input().split()))
        c_o ,c_e = 0, 0
        for i in li:
            if i%2:
                c_o += 1
            else:
                c_e += 1
        result = math.ceil(n/2)
        result_2 = math.floor(n/2)
        ans = min(c_o,result_2) + min(c_e,result)
        print(ans)
except:
    pass
'''
