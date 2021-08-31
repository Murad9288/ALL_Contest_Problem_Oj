import math
try:
    T = int(input())
    for i in range(T):
        n = int(input())
        if 1<=T<=100 and 1<=n<=100:
            print(math.factorial(n))
        else:
            break
except:
    pass
