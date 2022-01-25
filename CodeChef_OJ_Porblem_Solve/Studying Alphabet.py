s = str(input())
for _ in range(int(input())):
    w = str(input())
    for i in w:
        if i not in s:
            print("No")
            break
    else:
        print("Yes")
