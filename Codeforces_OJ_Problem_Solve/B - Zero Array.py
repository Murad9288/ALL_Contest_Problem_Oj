n = int(input())
arr = list(map(int,input().split()))[:n]
if sum(arr)%2==0 and sum(arr)//2>=max(arr):
    print("YES")
else:
    print("NO")
