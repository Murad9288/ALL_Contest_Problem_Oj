for _ in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    maxi_c = 1
    for i in range(n):
        while (li[i] % 2 == 0):
            li[i] //= 2
            maxi_c *= 2
    li.sort()
    li[-1] *= maxi_c
    print(sum(li))
