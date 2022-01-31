h, w = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(h)]
for row in zip(*mat):
    print(*row)
