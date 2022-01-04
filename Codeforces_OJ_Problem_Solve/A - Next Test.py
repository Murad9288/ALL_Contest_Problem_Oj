n = int(input())
arr = list(map(int,input().split()))[:n]
for i in range(1,3002):
    if i not in arr:
        print(i)
        break
