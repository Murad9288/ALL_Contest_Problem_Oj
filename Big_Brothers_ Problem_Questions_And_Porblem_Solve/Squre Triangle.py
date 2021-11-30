# F..Tin Guti..
for ind in range(int(input())):
     n = int(input())
     r = n // 2
     nm = n-1
     l = []
     for i in range(r + 1):
          if i == 0:
               print("*" * nm)
          elif i < r:
               a = "*" + (' ' * (i - 1)) + '*' + ' ' * (r - i - 1) +  ' ' * (r - i - 1) + "*" + (' ' * (i - 1)) + "*"
               l.append(a)
               print(a)

     for i in range(r - 2, -1, -1):
          s = ''
          for j in l[i]:
               s += j
          print(s)
     print("*" * nm)
     print()
