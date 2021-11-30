#intput:
'''
2
5
3 4 6 1 2
1
'''
'''
4
7 6 89 8
89
'''
#output:
'''
3
'''
'''
2
'''
# class chara korano hoyeche..
'''
l = list(map(int,input().split()))
n = int(input())
if n in l:
     print(l.index(n))
'''
class Solution:
    def search(self,A,N,x):
        if x in A:
            return A.index(x)
        return -1
import math

def main():
     T = int(input())
     while (T>0):
          N = int(input())
          A = list(map(int,input().split()))
          x = int(input())
          ob = Solution()
          print(ob.search(A,N,x))
          T -= 1
if __name__ == "__main__":
     main()

# nije kora hoyeche...
'''
class Solution:
     def seach(self,a,n,x):
          if x in a:
               return a.index(x)
          return n


import math
def main():
     for T in range(int(input())):
          n = int(input())
          a = list(map(int,input().split()))
          x = int(input())
          ob = Solution()
          print(ob.seach(a,n,x))
if __name__ == "__main__":
     main()
'''

