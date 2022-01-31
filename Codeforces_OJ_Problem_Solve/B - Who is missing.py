n = int(input())
arr = list(map(int,input().split()))
c = 0
for i in arr:
    c ^= i
print(c)
