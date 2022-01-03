try:
    for _ in range(int(input())):
        arr = []
        n = int(input())
        for i in range(n):
            li = list(map(int, input().split()))
            arr.append(li)
        for j in range(n - 2, -1, -1):
            for k in range(0, j + 1):
                arr[j][k] += max(arr[j + 1][k], arr[j + 1][k + 1])
        print(arr[0][0])
except:
    pass
