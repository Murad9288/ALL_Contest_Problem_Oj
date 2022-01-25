n, a, b = map(int, input().split())
res = []
for i in range(n + 1):
    li = list(str(i))
    arr = []
    for j in li:
        arr.append(int(j))
    if a <= sum(arr) and sum(arr) <= b:
        res.append(i)
print(sum(res))
