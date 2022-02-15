for _ in range(int(input())):
    n = int(input())
    c = 0
    for i in range(n,0,-2):
        c += i*i
    print(c)
