for _ in range(int(input())):
	n = int(input())
	m = input()
	s = ''.join(sorted(m))
	res_li = []
	# 1st step.
	for i in range(n):
		if s[i]!=m[i]:
			res_li.append(i+1)
	# 2nd step.
	if len(res_li)>0:
		print(1)
		print(len(res_li),end=" ")
		for i in res_li:
			print(i,end=" ")
		print()

	else:
		print(0)


