# Problem - 1: Contest Code:START11C / Problem Code:FACEDIR
# Problem name: Find the Direction.
# CodeChef.

try:
    for _ in range(int(input())):
        n = int(input())
        if n%4 == 1:
            print("East")
        elif n%4 == 2:
            print("South")
        elif n%4 == 3:
            print("West")
        else:
            print("North")
except:
    pass
