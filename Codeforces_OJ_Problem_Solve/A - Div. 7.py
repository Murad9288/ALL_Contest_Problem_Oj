for _ in range(int(input())):
    n = int(input())
    if n%7 == 0:
        print(n)
    else:
        k = n%7
        x = 7-k
        if n%10>=7:
            print(n-k)
        elif n%10 <=3:
            print(n+x)
        else:
            z = n%10
            if z>=k:
                print(n-k)
            else:
                print(n+x)
