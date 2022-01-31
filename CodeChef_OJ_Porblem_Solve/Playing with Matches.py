try:
    for _ in range(int(input())):
        a,b = map(int,input().split())
        arr = []
        for i in str(a+b):
            x = int(i)
            if x == 4:
                arr.append(4)
            elif x == 1:
                arr.append(2)
            elif x == 2 or x == 3 or x == 5:
                arr.append(5)
            elif x == 6 or x == 9 or x == 0:
                arr.append(6)
            elif x == 7:
                arr.append(3)
            else:
                arr.append(7)
        print(sum(arr))
except:
    pass
