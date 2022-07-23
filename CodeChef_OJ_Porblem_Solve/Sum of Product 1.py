# First system:

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    res = 0
    c = 0
    for i in range(n):
        if arr[i] == 1:
            c += 1
        else:
            res += c*(c+1)//2
            c = 0
    res += c*(c+1)//2
    print(res)
    
# Second system:

'''
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    res = 0
    c = 0
    for i in range(n):
        if arr[i] == 0:
            c = 0
        else:
            c += 1
        res += c
    print(res)
'''
