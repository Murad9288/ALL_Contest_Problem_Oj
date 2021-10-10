def main():
	n = int(input())
	arr = []
	for i in range(2):
		arr.append(list(input()))

	for i in range(n):
		if arr[0][i] == '1' and arr[1][i] == '1':
			print("NO")
			return

	print("YES")




if __name__ == '__main__':
	t = int(input())
	for i in range(t):
		main()