for _ in range(int(input())):
    s = input()
    n = len(s)
    res = ""
    c = -1
    for i in range(1,n):
        sum = int(s[i-1])+int(s[i])
        sum = str(sum)
        if len(sum) == 2:
            c = i
    if c != -1:
        i = 0
        while i<n:
            if i == c-1:
                sum = int(s[i])+int(s[i+1])
                sum = str(sum)
                res += sum
                i += 2
            else:
                res += s[i]
                i += 1
        print(res)
    else:
        x = s[2::]
        a,b = int(s[0]),int(s[1])
        y = str(a+b)
        print(y+x)
