# Problem : 1
# The Old Saint And Three Questions:
# Problem code: THREEQ

try:
    for _ in range(int(input())):
        li = list(map(int,input().split()))
        li_2 = list(map(int,input().split()))
        x = 0
        y = 0
        a = 0
        b = 0
        for i in li:
            if i == 1:
                x += 1
            elif i == 0:
                y += 1
        for j in li_2:
            if j == 1:
                a += 1
            elif j == 0:
                b += 1
        if x == a and y == b:
            print("Pass")
        else:
            print("Fail")
except:
    pass
