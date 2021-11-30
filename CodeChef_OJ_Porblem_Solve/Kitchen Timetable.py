try:
    
    for _ in range(int(input())):
        n = int(input())
        li = list(map(int,input().split())) [:n] # n limited
        li_2 = list(map(int,input().split())) [:n] # n limited
        c = 0
        for j in range(n):
            if j == 0 and li[j] >= li_2[j]:
                c += 1
            else:
                if li[j] - li[j-1] >= li_2[j]:
                    c += 1
        print(c)
except:
    pass
