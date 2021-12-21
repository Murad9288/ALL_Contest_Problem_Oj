import math
for _ in range(int(input())):
    n = int(input())
    for i in range(2,n):
        res = n-i-1
        if math.gcd(i,res) == 1:
            print(i,res,1)
            break
