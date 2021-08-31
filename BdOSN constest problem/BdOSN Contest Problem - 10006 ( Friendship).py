# problem  number: 10006
t = int(input())
for _ in range(t):
    L,R = map(int,input().split())
    start = 1
    stop = R
    R -= L - 1
    while start <= stop:
        if L <= start <= stop:
            R -= 1
        start = start * 2
    print(R)
