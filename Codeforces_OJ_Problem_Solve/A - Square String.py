s = []
for _ in range(int(input())):
    s.append(str(input()))
for i in s:
    x = len(i) // 2
    if i[x:] == i[:x]:
        print("YES")
    else:
        print("NO")
