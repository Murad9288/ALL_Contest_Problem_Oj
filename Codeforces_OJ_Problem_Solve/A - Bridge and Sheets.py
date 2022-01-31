N, L, W = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(L)
c = 0
res = []
for i in arr:
    if c < i:
        res.append(i-c)
        c = i + W
    else:
        c = i + W
r = 0
for j in res:
    r += -(-j//W)
print(r)
