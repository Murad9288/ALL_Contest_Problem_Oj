try:
    n = int(input())
    if n // 10 == 0:
        print("1")
    elif n // 100 == 0:
        print("2")
    elif n // 1000 == 0:
        print("3")
    else:
        print("More than 3 digits")
except:
    pass
