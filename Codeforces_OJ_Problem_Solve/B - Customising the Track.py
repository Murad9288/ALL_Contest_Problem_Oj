for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    res = sum(li)%len(li)
    print(res*(n-res))
