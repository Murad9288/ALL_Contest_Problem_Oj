arr = list(map(int,input().split()))
n = len(arr)
prefix_sum = []
for i in range(n+1):
    prefix_sum.append(i)
#prefix_sum = [0 for i in range(n+1)]
prefix_sum[0] = arr[0]
for i in range(1,n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]
for i in range(n):
    print(prefix_sum[i]," ",end="")
