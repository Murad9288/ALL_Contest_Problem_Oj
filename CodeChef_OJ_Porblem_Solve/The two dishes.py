# Problem = 2: Contest Code:START11C / Problem Code:MAX_DIFF
# Problem name: The two dishes.
try:
    for _ in range(int(input())):
        n,s = map(int,input().split())
        if (s <= n):
            res = s - 0
        else:
            c_res = s-n
            res = n - c_res
        print(res)
except:
    pass
