def solution(b,c):
    if c == 0:
        return b
    return solution(c,b%c)

for _ in range(int(input())):
    b,c = map(int,input().split())
    print(c//solution(b,c))
