for _ in range(int(input())):
    a, b, c = map(int, input().split())
    x, y = -1, -1
    if a < c:
        x = 1 
    if c < b * a:
        y = b
    print(x, y)
