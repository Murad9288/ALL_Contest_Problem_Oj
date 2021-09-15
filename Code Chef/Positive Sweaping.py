# Problem = 5:
# Problem name: Positive Sweping.
try:
    for _ in range(int(input())):
        n = int(input())
        li = list(map(int,input().split()))
        result = max(li)
        res = (((10**5)-result)+((10**5)-result+1))
        print(res)
except:
    pass
