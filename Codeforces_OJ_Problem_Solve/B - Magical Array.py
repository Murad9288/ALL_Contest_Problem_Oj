n = int(input())
arr = list(map(int,input().split()))[:n]
c = s = res = 0
for i in arr:
    c = (s==i)*c+1
    s = i
    res += c
print(res)
