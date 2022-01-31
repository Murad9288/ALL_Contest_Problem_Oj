import math
 
a=int(input())
if a<(2**31) and a>=(-1)*(2**31):
  print("Yes")
else:
  print("No")
