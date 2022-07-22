# name: MD Murad Hossain
# Eamil: muradhossainm01@gmail.com
# Accepted ho ja:

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    arr_2 = sorted(arr)
    arr_3 = [arr.index(arr_2[0]),0]
    null_arr = [0]*n
    # loop:
    for i in range(2):
        arr_3[0] = 0
        # while condition:
        while arr_3[0] < n:
            # checking not same:
            if not null_arr[arr_3[0]] and arr[arr_3[0]] == arr_2[arr_3[1]]:
                null_arr[arr_3[0]] = 1
                arr_3[0] += 1
                arr_3[1] += 1
            else:
                arr_3[0] += 1
    # current check:
    if arr_3[0] == arr_3[1]:
        print("YES")
    else:
        print("NO")
# Program Finnished.
