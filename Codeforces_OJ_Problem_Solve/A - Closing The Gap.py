for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    s = sum(arr)
    if(s % n == 0):
        print("0")
    else:
        print("1")
