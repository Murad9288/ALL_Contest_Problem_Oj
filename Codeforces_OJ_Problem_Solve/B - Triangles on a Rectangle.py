# Name: MD Murad Hossain
# Email - muradhossainm01@gmail.com
 
for _ in range(int(input())):
    # Input driver:
    w,h = map(int,input().split())
    d = list(map(int,input().split()))
    c = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = list(map(int,input().split()))
    # Weight part:
    res_w1 = (a[-1] - a[1]) * w
    res_w2 = (b[-1] - b[1]) * w
 
    # Height part:
    res_h1 = (c[-1] - c[1]) * h
    res_h2 = (d[-1] - d[1]) * h
 
    # Now print max element:
    print(max(res_w1,res_w2,res_h1,res_h2))
