for _ in range(int(input())):
    s = input()
    if(s.count('a') == 0 or s.count('b')==0):
        print(0)
    else:
        print(min(s.count('a'),s.count('b')))
