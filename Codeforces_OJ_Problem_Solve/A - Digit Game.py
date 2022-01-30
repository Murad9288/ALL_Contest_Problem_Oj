for _ in range(int(input())):
    n = int(input())
    s = input()
    r = []
    for i in s[0::2]:
        r.append(int(i))
    b = []
    for j in s[1::2]:
        b.append(int(j))
    #print(r)
    #print(b)
    win = 0
    if n % 2 == 1:
        win = 2
        for i in r:
            if i % 2 == 1:
                win = 1
                break
    else:
        win = 1
        for i in b:
            if i % 2 == 0:
                win = 2
                break
    print(win)
