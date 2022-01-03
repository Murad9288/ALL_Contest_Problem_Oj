try:
    for _ in range(int(input())):
        s = str(input())
        if s == "B" or s == "b":
            print("BattleShip")
        elif s == "C" or s == "c":
            print("Cruiser")
        elif s == "D" or s == "d":
            print("Destroyer")
        elif s == "F" or s == "f":
            print("Frigate")
        else:
            print("Not Found!")
except:
    pass
