try:
    while True:
        n = int(input())
        if n == 0:
            break
        arr = list(map(int, input().split()))
        res = [0] * len(arr)
        for i in range(len(arr)):
            res[arr[i] - 1] += i + 1
        if arr == res:
            print("ambiguous")
        else:
            print("not ambiguous")

except:
    pass
