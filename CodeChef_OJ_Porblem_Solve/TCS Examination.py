try:
    for _ in range(int(input())):
        d,t,c = map(int,input().split())
        d2,t2,c2 = map(int,input().split())
        total = d+t+c
        total2 = d2+t2+c2
        if total>total2:
            print("Dragon")
        elif total<total2:
            print("Sloth")
        else:
            if d>d2:
                print("Dragon")
            elif d<d2:
                print("Sloth")
            else:
                if t>t2:
                    print("Dragon")
                elif t<t2:
                    print("Sloth")
                else:
                    print("Tie")
except:
    pass
