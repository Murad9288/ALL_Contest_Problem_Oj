n = int(input())
arr = sorted(list(map(int,input().split())))
a = arr[::-1]
print(sum(a[0::2])-sum(a[1::2]))
