while True:
    n=int(input('Enter a number:\n'))
    if n<0:
        if n%2 == -0:
            print('Even Negetive')
        elif n%2 == -1:
            print('Odd Negetive')
            break
    else:
        print('Even')
    if n%2 == 0:
        print('Even Positive')
    elif n%2 == 1:
        print('Odd')
