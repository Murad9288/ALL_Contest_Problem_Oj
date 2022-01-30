try:
    for _ in range(int(input())):
        s = str(input())
        x = list(set(s))
        arr = []
        for i in x:
            arr.append(s.count(i))
        if (max(arr) * 2) == len(s):
            print("YES")
        else:
            print("NO")
except:
    pass
