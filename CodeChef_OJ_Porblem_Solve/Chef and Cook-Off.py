try:
    for _  in range(int(input())):
        a, b, c, d, e = map(int, input().split())
        res = a+b+c+d+e
        if res == 0:
            print("Beginner")
        elif res == 1:
            print("Junior Developer")
        elif res == 2:
            print("Middle Developer")
        elif res == 3:
            print("Senior Developer")
        elif res == 4:
            print("Hacker")
        elif res == 5:
            print("Jeff Dean")
except:
    pass
