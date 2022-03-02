for _ in range(int(input())):
    n = int(input())
    arr = []
    for i in range(1,n,2):
        arr.append(i+1)
        arr.append(i)
    if n % 2 == 1:
        arr.append(arr[-1])
        arr[-2] = n
    print(*arr)
