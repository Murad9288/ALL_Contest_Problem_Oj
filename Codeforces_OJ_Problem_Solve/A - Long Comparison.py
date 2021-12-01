for _ in range(int(input())):
    x,p = map(int,input().split())
    y,q = map(int,input().split())
    if x<y:
        while x<y:
            x *= 10
            p -= 1
    else:
        while x>y:
            y *= 10
            q -= 1
    if x == y:
        if p == q:
            print("=")
        elif p<q:
            print("<")
        else:
            print(">")
    if x>y:
        if p >= q:
            print(">")
        else:
            print("<")
    if x<y:
        if p <= q:
            print("<")
        else:
            print(">")





# 2nd System:
'''
for _ in range(int(input())):
    x,p = map(int,input().split())
    y,q = map(int,input().split())
    m = min(p,q)
    p = p-m
    q = q-m
    m_p = min(10,p)
    m_q = min(10,q)
    res_1 = x*(10**p)
    res_2 = y*(10**q)
    if res_1 > res_2:
        print(">")
    elif res_1 < res_2:
        print("<")
    else:
        print("=")
'''
