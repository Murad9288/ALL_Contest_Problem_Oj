for _ in range(int(input())):
    s = input()
    s2 = input()
    for i in range(len(s)):
        if s2 in (s[:i] + s[i::-1]):
            print("YES")
            break
    else:
        print("NO")

