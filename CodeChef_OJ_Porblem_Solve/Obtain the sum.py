# Problem 3: Contest Code:START11C / Problem Code:BIGARRAY
# Problem name: Obtain the sum.

try:
    for _ in range(int(input())):
        n,s = map(int,input().split())
        sum = 0
        result = (n*(n+1))//2
        if result > s:
            sum = result - s
        if (sum >= 1 and sum <= n):
            print(sum)
        else:
            print(-1)
except:
    pass
