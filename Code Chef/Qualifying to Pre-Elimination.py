# Contest name: SnackDown Practice Contest: Beginner -2021 (code:SDPCB21) 
# Problem code: QUALPREL
try:
    for _ in range(int(input())):
        N,K = map(int,input().split())
        L = list(map(int,input().split()))
        sort_list = sorted(L)
        rev = sort_list[::-1]
        c = 0
        for i in rev:
            if(i>=rev[K-1]):
                c += 1
        print(c)
except:
    pass
