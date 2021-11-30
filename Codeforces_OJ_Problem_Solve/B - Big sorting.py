n = int(input().strip())
unsorted = []
lengths = []

for k in range(n):
    number = str(input().strip())
    unsorted.append(number)
    lengths.append(len(number))

biglist = zip(lengths,unsorted)

for i in sorted(biglist):
    print(i[1])
