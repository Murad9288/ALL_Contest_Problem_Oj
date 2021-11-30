from math import gcd
try:

    def coprime(a, n):
        l = [0] * n
        if (n == 1):
            l[0] = 1
            return l
        for i in range(n):
            for j in range(i, n):
                if (gcd(a[i], a[j]) == 1):
                    l[i] = 1
                    l[j] = 1
        return l


    for _ in range(int(input())):
        n = int(input())
        a = [int(i) for i in input().split()]
        l = coprime(a, n)
        res = 0
        for i in l:
            if (i == 0):
                res = 1
                if (a[i] == 47):
                    a[i] = 46
                else:
                    a[i] = 47
                break
        print(res)
        print(*a)
except:
    pass
