# Contest Code:PRACTICE / Problem Code:BALLOON
try:
    for _ in range(int(input())):
        n = int(input())
        li =list(map(int,input().split()))
        sum,count = 0,0
        for i in li:
            if i<=7 and i>=1:
                count += 1
            sum += 1
            if count == 7:
                print(sum)
                break
except:
    pass
