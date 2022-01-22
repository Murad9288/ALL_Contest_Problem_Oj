try:
    l = int(input())
    b = int(input())
    area = l*b
    p = 2*(l+b)
    if area>p:
        print("Area\n%d"%area)
    elif area<p:
        print("Peri\n%d"%p)
    else:
        print("Eq\n%d"%p)

except:
    pass
