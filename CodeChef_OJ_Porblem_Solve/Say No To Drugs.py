try:
    for _ in range(int(input())):
        n,k,l = map(int,input().split())
    
        speeds = list(map(int,input().split()))
        
        if k > 0:
            speeds[-1] += k*(l-1)
            
            
        max_speed = max(speeds)
        
        if speeds.count(max_speed) > 1:
            print("No")
        elif speeds[-1] == max_speed:
            print("Yes")
        else:
            print("No")
except:
    pass
