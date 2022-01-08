try:
    n = int(input())
    l = list(map(int, input().split()))
    even = 0
    odd = 0
    for i in l:
        if (i % 2 == 0):
            even += i
        else:
            odd += i
    if (even > odd):
        print("READY FOR BATTLE")
    else:
        print("NOT READY")
except:
    pass
