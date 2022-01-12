try:
    for _ in range(int(input())):
        s = input()
        n = len(s)
        if n == 1:
            print("NO")
            continue
        c = 0
        d = -1
        i = 0
        while i<n:
            if s[i] == "1":
                c += 1
                d = i+1
            i += 1
        if c == 0 or (c == 1 and d == n):
            print("NO")
        else:
            print("YES")

except:
    pass
