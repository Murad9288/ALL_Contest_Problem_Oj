for _ in range(int(input())):
  n=int(input())
  a=list(map(int,input().split()))
  a.append(0)
  opr=0
  for i in range(1,len(a)-2):
    if(a[i]>a[i-1] and a[i]>a[i+1]):
      opr+=1
      a[i+1]=max(a[i],a[i+2])
  print(opr)
  a=a[:len(a)-1]
  print(*a)
