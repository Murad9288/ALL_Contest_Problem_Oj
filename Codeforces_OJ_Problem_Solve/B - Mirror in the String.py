for _ in range(int(input())):
    n = int(input())
    s = str(input())
    res = s[0]
    c = s[0]
    r = c
    if n>1:
        if s[0] == s[1]:
            print(s[0]+s[1])
        else:
            for i in range(1,len(s)):
                if s[i] <= c:
                    res += s[i]
                else:
                    break
                c = s[i]
            print(res+res[::-1])
    else:
        print(s[0]+s[0])
