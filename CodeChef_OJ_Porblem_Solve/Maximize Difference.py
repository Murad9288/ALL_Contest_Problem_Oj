# MD Murad Hossain
# Gamil: muradhossainm01@gmail.com
# Accepted Ho ja:

try:
    for _ in range(int(input())):
        n,m = map(int,input().split())
        if m < 2*n:
            print(m,m)
        elif m >= 2*n and m%n == 0:
            print(m,n)
        else:
            res = 0
            res_2 = 0
            div = m//2
            if m >= 2*n:
                div = 2*n
            Min = 0
            for i in range(n,div):
                d = m//i
                c_Min = (i*d)-i
                if c_Min > Min:
                    res = i
                    res_2 = i*d
                    Min = c_Min
            print(res,res_2)
except:
    pass
