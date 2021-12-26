from sys import stdin
 
t = int(input())
 
for _ in range(t):
    n,x = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    unswappable = a[n-x:x]
    a.sort()
    if a[n-x:x] == unswappable:
        print("YES")
    else:
        print("NO")
