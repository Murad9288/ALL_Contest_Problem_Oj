# Vaiyer problem.. eikhane intput newa lagbe jmn [11 11 14 11 11]. orthart sobgulo input ek thakbe.shudhu matro ekta songkha alada hobe... r oi alada songkhatike output a dekhabe...
'''
li = list(map(int,input().split()))
res = []

for i in li:
    if i not in res:
        res.append(i)
a = res[0]
b = res[1]

aa = li.count(a)
bb = li.count(b)
if aa > bb:
     print(b)
else:
     print(a)
'''
# eita eivabew kora jabe..

li = list(map(int,input().split()))
res = []

for i in li:
    if i not in res:
        res.append(i)
a = res[0]
b = res[1]
if li.count(a) < li.count(b):
    print(a)
else:
    print(b)


