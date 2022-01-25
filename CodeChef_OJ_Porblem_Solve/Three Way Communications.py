try:
    for _ in range(int(input())):
        d = int(input())
        c1 = list(map(int,input().split()))
        c2 = list(map(int,input().split()))
        c3 = list(map(int,input().split()))
        a = ((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2) ** 0.5
        b = ((c1[0] - c3[0]) ** 2 + (c1[1] - c3[1]) ** 2) ** 0.5
        c = ((c3[0] - c2[0]) ** 2 + (c3[1] - c2[1]) ** 2) ** 0.5
        if (a <= d and b <= d) or (c <= d and b <= d) or (a <= d and c <= d):
            print('yes')
        else:
            print('no')
except:
    pass
