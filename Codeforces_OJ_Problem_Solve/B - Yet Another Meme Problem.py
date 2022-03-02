n = int(input())
def solve(b):
    if b < 9:
        return 0
    elif b < 99:
        return 1
    elif b < 999:
        return 2
    elif b < 9999:
        return 3
    elif b < 99999:
        return 4
    elif b < 999999:
        return 5
    elif b < 9999999:
        return 6
    elif b < 99999999:
        return 7
    elif b < 999999999:
        return 8
    elif b <= 1000000000:
        return 9
for _ in range(n):
    a, b = map(int,input().split())
    c = solve(b)
    print(a * c)
