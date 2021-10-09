s = input()
u = 0
l = 0
for char in s:
    if ord(char) in range(ord('A'), ord('Z') + 1):
        u += 1
    else:
        l += 1
print(s.lower() if (l >= u) else s.upper())

