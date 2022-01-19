try:
    s = str(input())
    vow = "aeiou"
    for i in s.lower():
        if i in vow:
            print("Vowel")
        else:
            print("Consonant")
except:
    pass
