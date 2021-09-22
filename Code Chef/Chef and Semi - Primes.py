try:
    def isprime(n):
        if n%2==0:
            return False 
        for j in range(3, int(n**0.5)+1, 2):
            if n%j==0:
                return False 
        return True
    arr = []
    for i in range(3, 201):
        if i%2==0 and isprime(i/2):
            arr.append(i)
            continue
        for j in range(3, int(i**0.5)+1, 2):
            if i%j==0 and isprime(j) and isprime(i//j) and i!=j and i//j != j:
                arr.append(i) 
    
    for _ in range(int(input())):
        n = int(input())
        for j in range(len(arr)):
            if n-arr[j] in arr:
                print("YES")
                break
        else:
            print("NO")
except:
    pass
