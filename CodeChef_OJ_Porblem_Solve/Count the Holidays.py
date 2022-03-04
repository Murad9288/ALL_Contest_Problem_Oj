for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    arr2 = [6,7,13,14,20,21,27,28]
    print(len(set(arr+arr2)))
