for _ in range(int(input())):
    n = int(input())
    l = list(map(int,input().split()))
    count = 0
    for i in l:
        if i%2 != 0:
            count += 1
    if count == n:
        print("Yes")
    else:
        print("No")
