# Freauence of Limited Problem..

for _ in range(int(input())):
    N = int(input())
    arr = [int(x) for x in input().strip().split()]
    P = int(input())
    for i in range(N):
        arr[i] = arr[i]-1
    arr.sort()
    index = N
    for i in range(N):
        if arr[i]>=N:
            arr[i] = 0
            if index == N:
                index = i
    for i in range(index):
        arr[arr[i]%N] = int(arr[arr[i]%N]+N)
    
    for i in range(N):
        arr[i] = arr[i]//N
    for k in arr:
        print(k,end=" ")

        
  
