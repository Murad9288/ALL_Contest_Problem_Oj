try:
    for _ in range(int(input())):
        n,a = map(int,input().split())
        if n == 1:
            if a%2 == 0:
                print("Even")
            else:
                print("Odd")
        elif a%2 == 1:
            if n%2 == 0:
                print("Even")
            else:
                print("Odd")
        else:
            print("Impossible")
except:
    pass
