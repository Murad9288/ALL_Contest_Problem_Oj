def prob231A_Team():
  n, count = int(input()), 0
  for _ in range(n):
    if sum(int(x) for x in input().split()) > 1:
      count += 1
  return count
print(prob231A_Team())
