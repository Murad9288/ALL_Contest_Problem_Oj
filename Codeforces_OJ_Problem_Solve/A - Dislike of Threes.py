li = []
i = 1
while len(li) < 1001:
    if i % 10 != 3 and i % 3 != 0:
        li.append(i)
    i += 1
for _ in range(int(input())):
    k = int(input())
    print(li[k - 1])
