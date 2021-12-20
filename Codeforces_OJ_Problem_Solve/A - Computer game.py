def computer_game():
    n = int(input())
    li = []
    for j in range(2):
        li.append(list(input()))
    for i in range(n):
        if li[0][i] == "1" and li[1][i] == "1":
            print("NO")
            return
    print("YES")
for _ in range(int(input())):
    computer_game()
