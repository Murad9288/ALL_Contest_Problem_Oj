a = str(input())
b = str(input())
c = str(input())
add = list(a+b+c)
if add == add[::-1]:
    print("YES")
else:
    print("NO")
