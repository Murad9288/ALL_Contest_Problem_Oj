def solve():
	n, m = map(int, input().split(' '))
	a = list(input())

	num = 0
	for i in range(n - 2):
		if (''.join(a[i:i + 3]) == 'abc'):
			num += 1

	for i in range(m):
		index, ch = input().split(' ')
		index = int(index) - 1

		for j in range(max(0, index - 2), index + 1):
			if (''.join(a[j:j + 3]) == 'abc'):
				num -= 1

		a[index] = ch

		for j in range(max(0, index - 2), index + 1):
			if (''.join(a[j:j + 3]) == 'abc'):
				num += 1

		print(num)

solve()
