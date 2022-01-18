try:
    for _ in range(int(input())):
        s = str(input())
        mid = len(s)//2
        if len(s)%2 == 0:
            s1 = s[:mid]
            s2 = s[mid:]
        else:
            s1 = s[:mid]
            s2 = s[mid+1:]
        res = sorted(s1)
        res2 = sorted(s2)
        if res == res2:
            print("YES")
        else:
            print("NO")
except:
    pass
