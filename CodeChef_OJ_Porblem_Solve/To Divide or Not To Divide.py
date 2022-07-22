def solution(a,b,n):
    if a%b == 0:
        return -1
    c = n
    if c%a != 0:
        c = n+a-(c%a)
    while not(c%a == 0 and c%b !=0):
        c += a
    return c
for _ in range(int(input())):
    a,b,n = map(int,input().split())
    print(solution(a,b,n))
