n = int(input())
a = list(map(int,input().split()))
s = sum(a)
arr = []
for i in a:
    if i%2:
        arr.append(i)
if s % 2:
    print(s)
elif arr:
    print(s - min(arr))
else:
    print(0)
