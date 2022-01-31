s = str(input())
a,b = map(int,input().split())
arr = []
for i in s:
    arr.append(i)
arr[a-1],arr[b-1] = arr[b-1],arr[a-1]
print(*arr,sep="")
