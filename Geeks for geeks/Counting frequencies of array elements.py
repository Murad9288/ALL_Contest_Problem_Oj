def countFreq(arr,n):
    visited = [False for i in range(n)]
    for i in range(n):
        if visited[i] == True:
            continue
        count = 1
        for j in range(i+1,n,1):
            if (arr[i] == arr[j]):
                visited[j] = True
                count += 1
        print(arr[i], count)

# Driver code
if __name__ == "__main__":
    arr = list(map(int,input().split()))
    n = len(arr)
    countFreq(arr,n)

