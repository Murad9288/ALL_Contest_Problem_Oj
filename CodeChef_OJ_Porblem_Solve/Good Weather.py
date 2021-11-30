try:
    for _ in range(int(input())):
        li = list(map(int,input().split()))
        one = 0
        zero = 0
        for i in li:
            if i == 1:
                one += 1
            elif i == 0:
                zero += 1
            else:
                break
        if one > zero:
            print("YES")
        else:
            print("NO")
except:
    pass
