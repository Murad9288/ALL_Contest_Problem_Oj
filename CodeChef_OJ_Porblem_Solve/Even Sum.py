try:
    for _ in range(int(input())):
        size = int(input())
        l = list(map(int,input().split()))
        if sum(l)%2 == 0:
            print(1)
        else:
            print(2)
except:
    pass
