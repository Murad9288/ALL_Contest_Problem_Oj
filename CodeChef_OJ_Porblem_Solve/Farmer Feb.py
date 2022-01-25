try:
    def isprime(n):
        j = 1
        for i in range(1, n):
            if n % i == 0:
                j += 1
        if j == 2:
            return True
    for _ in range(int(input())):
        x, y = [int(x) for x in input().split()]
        j = 1
        while (isprime(x + y + j)) is not True:
            j += 1
        print(j)
except:
    pass
