M,N = map(int,input().split())
n = N // 2
x = M * n
if N % 2 == 0:
    y = x
else:
    m = M // 2
    y = x + m
print(y)
