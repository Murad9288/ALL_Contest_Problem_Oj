try:
    for _ in range(int(input())):
        n = input()
        show = input().replace(".", "")
        if show.count("HT")*2 == len(m):
            print("Valid")
        else:
            print("Invalid")
except:
    pass
