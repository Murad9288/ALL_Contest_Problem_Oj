for _ in range(int(input())):
    s = input()
    c = ""
    for i in range(len(s)):
        if i % 2 == 0:
            if s[i] == "a":
                c += "b"
                continue
            c += "a"
            continue
        if s[i] == "z":
            c += "y"
            continue
        c += "z"
    print(c)
