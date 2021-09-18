T = int(input())
for i in range(T):
    n,m = map(int,input().split())
    L = list(map(int,input().split()))# others way:list(map(int,input().split()))[m:]
    result = L[m:]
    print(sum(result))
    
            
   
