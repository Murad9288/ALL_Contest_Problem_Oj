import math
for _ in range(int(input())):
    n = int(input())
    i = n
    while 1:
        if math.gcd(i,sum(map(int,str(i))))>1:
            print(i)
            break
        i += 1
