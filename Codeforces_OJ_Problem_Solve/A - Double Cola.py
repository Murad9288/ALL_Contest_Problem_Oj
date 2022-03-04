n = int(input())
i = 1
while True:
    if n > i*5:
        n -= i*5
        i *= 2
    else:
        if n <= i:
            print("Sheldon")
        elif n <= 2*i:
            print("Leonard")
        elif n <= 3*i:
            print("Penny")
        elif n <= 4*i:
            print("Rajesh")
        else:
            print("Howard")
        exit(0)
