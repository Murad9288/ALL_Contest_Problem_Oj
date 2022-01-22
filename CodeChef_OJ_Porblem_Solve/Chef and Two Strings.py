try:
    for _ in range(int(input())):
        s1 = str(input())
        s2 = str(input())
        min = 0
        max = 0
        for i in range(len(s1)):
            if (s1[i] != s2[i] and (s1[i] != '?' and s2[i] != '?')):
                min += 1
            if ((s1[i] == '?' or s2[i] == '?') or (s1[i] == '?' and s2[i] == '?')):
                max += 1
        print(min, max+min)
except:
    pass
