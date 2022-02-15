for _ in range(int(input())):
    n,k = map(int,input().split())
    count = 0
    while n>0:
        if n%k == 0:
            count += 1
            n //= k
        else:
            count += n%k
            n -= n%k
    print(count)
