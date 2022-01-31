n = int(input())
h = list(map(int,input().split()))[:n]
c = 0
for i in range(n):
    if c < h[i]:
        c = h[i]
    else:
        break
print(c)
