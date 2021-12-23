for _ in range(int(input())):
     n = int(input())
     arr = list(map(int,input().split()))
     c = 0
     sum = 0
     for i in range(len(arr)):
          if arr[i] == 1:
               sum += 1
          elif arr[i] == 0:
               c += 1
          else:
               continue
     print((2**c)*sum)
