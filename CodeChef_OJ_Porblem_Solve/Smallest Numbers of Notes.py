try:
    for _ in range(int(input())):
        n = int(input())
        count = 0
        while n != 0:
            if n >= 100:

                count = n // 100
                n = n % 100
            elif n >= 50:
                count = count + (n // 50)
                n = n % 50
            elif n >= 10:
                count = count + (n // 10)
                n = n % 10
            elif n >= 5:
                count = count + (n // 5)
                n = n % 5
            elif n >= 2:
                count = count + (n // 2)
                n = n % 2
            else:
                count = count + (n // 1)
                n = n % 1
        print(count)
except:
    pass




