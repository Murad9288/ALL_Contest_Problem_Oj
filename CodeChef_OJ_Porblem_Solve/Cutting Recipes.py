try:
    import math
    for _ in range(int(input())):
        arr = list(map(int, input().split()))
        g = math.gcd(arr[1], arr[2])
        for i in range(3, len(arr)):
            g = math.gcd(g, arr[i])
        for j in range(1, len(arr)):
            print(arr[j] // g, end=" ")
        print()
except:
    pass
