#CodeChef problem: Sorting Segments.

try:
     for _ in range(int(input())):
          a,b = map(int,input().split())
          L = list(map(int,input().split()))
          n = len(L[:b])
          x = L[b:a]
          c = 0
          for i in range(1, n):
               item = L[i]
               j = i - 1
               while j >= 0 and L[j] > item:
                    L[j+1] = L[j]
                    j = j - 1
                    L[j+1] = item
                    c += 1
          if sorted(x) == x:
               print(c)
          else:
               if c > max(x):
                    print(c-max(x))
               else:
                    print(max(x)-c)
except:
     pass
