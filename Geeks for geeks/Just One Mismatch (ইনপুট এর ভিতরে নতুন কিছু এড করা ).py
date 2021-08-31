#Problem link:
#https://practice.geeksforgeeks.org/viewSol.php?subId=3154cece68ba98fb2c0c567c5c620818&pid=703564&user=muradhossainm01
# simple input:
'''
5
banaba apple orange mango chocolate
banana
'''
'''
4
a b c d
e
'''
# simple output:
'''
True
'''
'''
False
'''



# class baad diye.:
'''
N = int(input())
arr = input().split()
S = input()
count = 1
for i in range(N):
    count = 0
    if len(arr[i]) == len(S):
        for j in range(len(arr[i])):
            if arr[i][j] != S[j]:
                if count == 0:
                    count = 1
                else:
                    count = 0
    if count == 1:
        print("True")
        break
    else:
        print("False")
        break
'''

# class diye problem:

class Solution:
    def isStringExist (self, arr, N, S):
        count = 1
        for i in range(N):
            count = 0
            if len(arr[i]) == len(S):
                for j in range(len(arr[i])):
                    if arr[i][j] != S[j]:
                        if count == 0:
                            count = 1
                        else: 
                            count = 0
                            break
            if count == 1:
                return ("True")
        return ("False")
#  Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        S = input()
        ob = Solution()
        print(ob.isStringExist(arr, N, S))
