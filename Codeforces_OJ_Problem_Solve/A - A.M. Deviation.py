for _ in range (int(input())):
    li = []
    s = int(sum(map(int,input().split())))
    if(s%3==0):
        li.append(0)
    else:
        li.append(1)
    print(*li)
