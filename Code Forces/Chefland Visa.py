# CodeChef er problem:
#Chefland Visa

try:
    for _ in range(int(input())):
        x1,x2,y1,y2,z1,z2 = map(int,input().split())
        if 20<=x1 and x2<=50 and 1900<=y1 and y2<=2100 and 1<=z1 and z2<=6:
            if x1<=x2 and y1<=y2 and z1>=z2:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
except:
    pass



