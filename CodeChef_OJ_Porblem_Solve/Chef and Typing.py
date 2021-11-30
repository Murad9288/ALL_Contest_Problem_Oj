try:
    for _ in range(int(input())):
        sum = 0
        w = []
        for i in range(int(input())):
            s = input()
            w.append(s)
            t = 2
            l = ["d","f"]
            r = ["j","k"]
            for j in range(1,len(s)):
                if (s[j-1] in l) and (s[j] in l) or (s[j-1] in r) and (s[j] in r):
                    t += 4
                else:
                    t += 2
            if w.count(s) > 1:
                t //= 2
            sum += t
        print(sum)
except:
    pass
