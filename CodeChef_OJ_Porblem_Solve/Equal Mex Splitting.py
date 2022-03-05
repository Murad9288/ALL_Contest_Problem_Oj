for _ in range(int(input())):
   n = int(input())
   arr = list(map(int,input().split()))
   s = 0
   for i in range(len(arr)):
       if arr[i] == 0:
           s += 1
   print(max(s, n - s))
