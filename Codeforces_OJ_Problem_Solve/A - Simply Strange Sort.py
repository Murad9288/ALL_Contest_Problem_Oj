for i in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split())) [:n]
    count = 0
    while 1:
        if arr == sorted(arr):
            break
        elif count%2==0:
            for i in range(0,n-1,2):
                if arr[i]>arr[i+1]:
                    # now swapping.
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            # now counting result.
            count += 1
        else:
            for i in range(1,n-1,2):
                if arr[i]>arr[i+1]:
                    # now swapping
                    arr[i],arr[i+1] = arr[i+1],arr[i]
            # now counting result.
            count += 1
    print(count)
