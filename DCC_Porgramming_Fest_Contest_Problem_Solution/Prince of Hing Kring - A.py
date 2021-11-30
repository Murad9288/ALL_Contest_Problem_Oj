# A 
a =input()
s = a.lower()
c = []
li=["a","e","i","o","u"]
for char in s:
    if char in li:
        c.append(char)
print(len(c))
