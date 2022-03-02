for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans = sum(arr)
    if ans%2 == 0:
        print('YES')
    else:
        print('NO')
