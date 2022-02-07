import math
for _ in range(int(input())):
    a,b = map(int,input().split())
    if b-a == 0:
        print(0)
    else:
        print(math.ceil(abs(b-a)/10))
