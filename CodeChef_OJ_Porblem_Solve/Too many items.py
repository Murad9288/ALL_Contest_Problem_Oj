# cook your dish here
for _ in range(int(input())):
    n = int(input())
    if n%10 == 0:
        print(n//10)
    else:
        print((n//10)+1)
