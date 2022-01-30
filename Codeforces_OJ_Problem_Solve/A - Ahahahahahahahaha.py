for _ in range(int(input())):
    a = int(input())//2
    b = input().split()
    if b.count("0")<b.count("1"):
        c ="1 "
        if a%2 == 1:
            a += 1
    else:
        c ="0 "
    print(a)
    print(a*c)
