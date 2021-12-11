try:
    for _ in range(int(input())):
        a,b,c,d = list(map(int,input().split()))
        chef = a+(c*10)
        chefina = b+(d*10)
        if chef > chefina:
            print("Chefina")
        elif chef < chefina:
            print("Chef")
        else:
            print("Draw")

except:
    pass
