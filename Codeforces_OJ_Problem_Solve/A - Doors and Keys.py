t = input()
arr = []
for i in range(int(t)):
    arr.append(input())
for i in arr:
    keyR = False
    keyG = False
    keyB = False
    R = False
    G = False
    B = False
    for j in i:
        if j == 'r':
            keyR = True
        elif j == 'g':
            keyG = True
        elif j == 'b':
            keyB = True
        elif j == 'R':
            R = keyR
        elif j == 'G':
            G = keyG
        elif j == 'B':
            B = keyB
    if R and G and B:
        print("YES")
    else:
        print("NO")
