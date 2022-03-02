# cook your dish here
for _ in range(int(input())):
    a,b = list(map(int,input().split()))
    if a+b>10:
        print(21-(a+b))
    else:
        print(-1)
