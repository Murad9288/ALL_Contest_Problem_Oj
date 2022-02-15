# cook your dish here
for _ in range(int(input())):
    li = []
    for i in range(int(input())):
        fn,ln = input().split()
        li.append(fn)
        li.append(ln)
    for i in range(0,len(li),2):
        if li.count(li[i]) != 1:
            print(li[i],li[i+1])
        else:
            print(li[i])
            
    
