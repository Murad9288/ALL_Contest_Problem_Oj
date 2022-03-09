for _ in range(int(input())):
    n = int(input())
    for i in range(1,n+1):
        print(i, end =" ")
        for j in range(n,0,-1):
            if j != i:
                print(j, end =" ")
        print()
