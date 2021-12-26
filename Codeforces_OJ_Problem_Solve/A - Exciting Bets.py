for _ in range(int(input())):
    a,b = map(int,input().split())
    if a==b:
        print(0,0)
    else:
        Max = abs(a-b) # abs() function er kaj holo duita songkhake biyog korle biyog foler moddhe minus chinno thakbena.
        #print("max:",Max)
        Min = min(a%Max,(Max-a)%Max)
        print(Max,Min)
