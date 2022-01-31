S = str(input())
x = 0
y = 0
if S == S[::-1]:
    print('Yes')
else:
    for i in range(len(S)):
        if S[i] != 'a':
            break
        x += 1
    for j in range(1, len(S)+1):
        if S[-j] != 'a':
            break
        y += 1
    S = 'a'*(y-x) + S
 
    if S == S[::-1]:
        print('Yes')
    else:
        print('No')
