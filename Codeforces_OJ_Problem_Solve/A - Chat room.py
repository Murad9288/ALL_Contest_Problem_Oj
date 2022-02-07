s = str(input())
c = 0
v = "hello"
for i in s:
    if i == v[c]:
        c += 1
    if c == 5:
        print("YES")
        break
else:
    print("NO")
