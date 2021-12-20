for _ in range(int(input())):
  n = int(input())
  result =[]
  i = 1
  while(i**2<=n):
    result.append(i**2)
    i += 1
  j = 1
  while(j**3<=n):
    result.append(j**3)
    j += 1
  print(len(set(result)))
