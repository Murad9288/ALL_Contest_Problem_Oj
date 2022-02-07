# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    words = input().split()
    arr = []
    for i in range(k):
        s = input().split()
        arr.append(s)
    for i in words:
        c = 0
        for x in arr:
            if (i in x):
                c += 1
        if (c > 0):
            print("YES",end=" ")
        else:
            print("NO",end=" ")
    print()
