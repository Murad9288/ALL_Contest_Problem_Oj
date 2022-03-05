for _ in range(int(input())):
    n ,m = map(int,input().split())
    if n >= m:
        print("YES")
    else:
        a = (n//2)+1
        b = (n-a+1)*a
        if(m>b):
            print("NO")
        else:
            cnt = 0
            for i in range(1,n+1):
                if m%i == 0 :
                    if n-i+1>=(m/i):
                        cnt = 1
                        break
            if cnt :
                print("YES")
            else:
                print("NO")
