# chocolate problem

'''
simple input and output:
3
2 1
1 2
1 # output
4 1
1 1 1 1
1  # output
5 3
50 50 50 100 100
2  # output
'''


for i in range(int(input())):
    n,x = map(int,input().split())

    li = list(map(int,input().split()))

    result = n - x
    s = list(set(li))
    if  len(s) <= result:
        print(result)
    else:
        print(len(s))
