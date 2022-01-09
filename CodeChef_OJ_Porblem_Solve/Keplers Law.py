try:
    for _ in range(int(input())):
        a,b,c,d = map(int,input().split())
        if (a**2)/(c**3) == (b**2)/(d**3):
            print("Yes")
        else:
            print("No")

except:
    pass
