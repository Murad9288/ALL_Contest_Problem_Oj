def AB_Balance1(s):
    ab = 0
    ba = 0
    for i in range(len(s) - 1):
        if s[i:i+2] == "ab":
            ab += 1
        elif s[i:i+2] =="ba":
            ba += 1
    return ab,ba
def AB_Balance2(s):
    ab,ba = AB_Balance1(s)
    if ab == ba:
        return s
    for i in range(len(s)):
        t = ""
        for j in range(len(s)):
            if i != j:
                t += s[j]
            else:
                t += "ab"[s[i] == "a"]
        ab, ba = AB_Balance1(t)
        if ab == ba:
            return t
for _ in range(int(input())):
    s = input()
    print(AB_Balance2(s))
