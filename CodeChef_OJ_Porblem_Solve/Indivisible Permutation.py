
try:
    for _ in range(int(input())):
        n = int(input())
        if n == 2:
            print(2,1)
        else:
            print(1,end=" ")
            for i in range(3,n+1):
                print(i,end=" ")
            print(2)
except:
    pass

