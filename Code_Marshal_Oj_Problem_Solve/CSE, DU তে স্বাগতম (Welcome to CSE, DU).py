x,y,z = map(int,input().split())
if x >= 0 and y >= 0 and z<=1000 and z <= x and z <= y:
     print((x+y)-z)
else:
     print("Wrong")

