s1 = input()
s2 = input()
res = ((int(s1[:2])+int(s2[:2]))*60+(int(s1[3:])+int(s2[3:])))//2
h3 = res//60
m3 = res-h3*60
res = ''
if h3<10:
  res += '0'
  res += str(h3)
else:
  res += str(h3)
res += ':'
if m3<10:
  res += '0'
  res += str(m3)
else:
  res += str(m3)
print(res)
