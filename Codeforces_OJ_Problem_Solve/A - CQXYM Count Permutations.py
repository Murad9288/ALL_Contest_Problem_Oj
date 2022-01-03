for _ in range(int(input())):
    n = int(input())
    c = 1
    limit = (10**9)+7
    for i in range(3,2*n+1):
        c = (c*i)%limit
    print(c%limit)
