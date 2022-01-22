n = int(input())
arr = list(map(int,input().split()))[:n]
c = max(arr)
s = 0
for i in arr:
    s = s+(c-i)
print(s)
