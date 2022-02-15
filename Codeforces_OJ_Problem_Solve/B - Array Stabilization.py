n = int(input())
arr = sorted(list(map(int,input().split()))[:n])
a = arr[n-2]-arr[0]
b = arr[n-1]-arr[1]
print(min(a,b))
