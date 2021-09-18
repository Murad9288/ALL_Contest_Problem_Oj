# B.MEXor Mixup

for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==b or a==0 or b == 0:
        print(a+b+1)
    elif a==1 or a==2 and 1<b:
        print(a+1)
    else:
        print(a)
