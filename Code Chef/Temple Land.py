#  Contest Code:PRACTICE / Problem Code:TEMPLELA

try:
    def Tamle_Land(li,n):
        if li[0] != 1:
            return "no"
        elif n%2 != 0 and li == li[::-1]:
            for i in range(n//2):
                if li[i]+1 != li[i+1]:
                    return "no"
        elif n%2 == 0 or li != li[::-1]:
            return "no"
        return "yes"  
    for _ in range(int(input())):
        n = int(input())
        li = list(map(int,input().split()))
        print(Tamle_Land(li,n))
except:
    pass
