for _ in range(int(input())):
    n,k = map(int,input().split())
    s = str(input())
    c = 0
    for i in range(n//2):
        if s[i] != s[n-i-1]:
            c += 1
    r = k-c
    if r>=0 and r%2 == 0 or r>=0 and n%2==1:
        print("YES")
    else:
        print("NO")
