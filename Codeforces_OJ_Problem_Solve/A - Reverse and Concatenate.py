for _ in range(int(input())):
    n,k = map(int,input().split())
    s = str(input())
    temp = s[::-1]
    if k == 0 or s == temp:
        print(1)
        continue
    print(2)
