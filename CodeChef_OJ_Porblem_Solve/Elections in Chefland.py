try:
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        if a>50 and b<=50 and c<=50:
            print("A")
        elif a<=50 and b>50 and c<=50:
            print("B")
        elif a<=50 and b<=50 and c>50:
            print("C")
        else:
            print("NOTA")
except:
    pass
