for _ in range(int(input())):
    a,b = map(int,input().split())
    if b*b <= a and a%2 == b%2:
        print("YES")
    else:
        print("NO")
