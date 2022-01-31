n,m = map(int,input().split())
s1 = input().split()
s2 = input().split()
s = set(s2)
for i in range(len(s1)):
    if s1[i] in s:
        print("Yes")
    else:
        print("No")
