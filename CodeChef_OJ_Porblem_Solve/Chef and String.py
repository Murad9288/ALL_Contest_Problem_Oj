try:
    for _ in range(int(input())):
        s = str(input())
        c = i = 0
        while i < len(s) - 1:
            if abs(ord(s[i]) - ord(s[i + 1])) == 1:
                c += 1
                i += 1
            i += 1
        print(c)
except:
    pass
