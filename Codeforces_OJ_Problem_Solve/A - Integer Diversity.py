for _ in range(int(input())):
    n = int(input())
    arr = [abs(int(i)) for i in input().split()]
    i = 0
    s = set()
    for e in arr:
        if e not in s:
            s.add(e)
            i += 1
        elif -e not in s:
            s.add(-e)
            i += 1
    print(i)
