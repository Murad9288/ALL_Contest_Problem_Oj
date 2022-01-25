n = int(input())
arr = list(map(int,input().split()))[:n]
c = 0
while True:
    for i in range(n):
        if arr[i] % 2 == 1:
            break
        arr[i] /= 2
    else:
        c += 1
        continue
    break
print(c)
