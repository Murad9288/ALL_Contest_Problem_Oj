for _ in range(int(input())):
    n = input()
    c = len(n)
    result = 0
    for i in range(c):
        for j in range(i+1,c):
            if int(n[i] + n[j]) %25 == 0:
                result = c-i-2
    print(result)
