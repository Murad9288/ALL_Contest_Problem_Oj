n = int(input())
s = input()
res = ""
j = 1
i = 0
while i<n:
    res += s[i]
    i += j
    j += 1
print(res)
