try:
    for _ in range(int(input())):
        n,d = list(map(int,input().split()))
        sum = 1
        for i in range(1,d+1):
            if i<=10:
                sum = sum*2
                if sum>n:
                    sum = n
                    break
            else:
                sum = sum*3
                if sum>n:
                    sum = n
                    break
        print(sum)

except:
    pass
