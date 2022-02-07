n = int(input())
arr = list(map(int,input().split()))
a,b = map(int,input().split())
year = 0
for i in range(a,b):
    year += arr[i-1]
print(year)
