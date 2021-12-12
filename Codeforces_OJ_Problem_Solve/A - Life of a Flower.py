# A - Life of a Flower
for _ in range(int(input())):
    c=1
    n=int(input())
    a=[int(i) for i in input().split()]
    for j in range(n):
        if j==0:
            c+=a[j]
        elif j>=1 and (a[j]==1 and a[j-1]==0):
            c+=1
        elif j>1 and a[j]==0 and a[j-1]==1:
            c+=0
        elif j>=1 and a[j]==1 and a[j-1]==1:
            c+=5
        elif j>=1 and a[j]==0 and a[j-1]==0:
            c=-1
            break
    print(c)
