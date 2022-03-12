for _ in range(int(input())):
    s = str(input()).upper()
    s2 = str(input()).upper()
    app = ""
    for i in range(len(s)):
        if s[i] == s2[i]:
            app += "G"
        else:
            app += "B"
    print(app)
