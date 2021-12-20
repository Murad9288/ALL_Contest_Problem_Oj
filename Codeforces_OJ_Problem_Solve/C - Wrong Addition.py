for _ in range(int(input())):
     a,n = map(int,input().split())
     c = 0
     for i in range(18):
          r = a%10
          t = n%10
          if r > t:
               c += (10**i) * (10 + t-r)
               n //= 10
    
               if n%10 != 1:
                    c = -1
                    break
          else:
               c += (10**i) * (t-r)
          n //= 10
          a //= 10
     print(c)
