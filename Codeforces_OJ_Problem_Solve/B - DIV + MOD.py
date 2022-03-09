for _ in range(int(input())):
    l,r,a = map(int,input().split())
    x = l//a
    tmi = r//a
    ami = r%a
    if x == tmi:
        print(ami+tmi)
    else:
        print(max(tmi+ami,tmi+a-2))
