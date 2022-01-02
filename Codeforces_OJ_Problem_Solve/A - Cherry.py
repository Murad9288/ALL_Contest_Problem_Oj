for _ in range(int(input())):
    n =  int(input())
    arr = list(map(int,input().split()))
    result = 0
    for i in range(n-1):
        result = max(result,arr[i] * arr[i+1])
    print(result)
