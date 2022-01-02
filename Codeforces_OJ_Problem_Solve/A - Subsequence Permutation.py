for _ in range(int(input())):
    n =  int(input())
    s = str(input())
    ss = sorted(s)
    c = 0
    #d = 0
    for i in range(n):
        if ss[i] != s[i]:
            c += 1
        #else:
            #d += 1
    print(c)
    #print(d)
