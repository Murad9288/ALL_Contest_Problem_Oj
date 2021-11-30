# problem link:
# ##https://practice.geeksforgeeks.org/problems/reverse-squared-sum/0/?fbclid=IwAR2IfiQFxipV258KjZxjfJovS-GfmeC_ATwPCiHY5hQdw24wC-c0GW2i_zc
#Simple input:
'''
2
3
1 2 3

5
4 8 1 2
'''
#simple output:
'''
6

51
'''
# code:
for t in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))

    res = arr[n-1] * arr[n-1]
    pormin = -1

    for i in range(n-2,-1,-1):
        res += pormin * arr[i] * arr[i]
        pormin *= -1

    print(res)
