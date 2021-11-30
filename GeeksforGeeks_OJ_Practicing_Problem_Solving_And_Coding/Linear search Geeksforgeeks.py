#Example Input and Output for Your Program:
#Input:
'''
2
4
1 2 3 4
3
'''
'''
5
10 90 20 30 40 
40
'''
#Output:
'''
2
'''
'''
4
'''
# Don't User defination(Function baad diye kora) :
'''
for T in range(int(input())):
     n = int(input())
     a = list(map(int,input().split()))
     x = int(input())
     for i in range(len(a)):
          if (x == a[i]):
               print(i)
'''
# User Defination diye kora(Function diye):
def linear_search(l,x):
     for i in range(len(l)):
          if x == l[i]:
               return i
for T in range(int(input())):
     n = int(input())
     l = list(map(int,input().split()))
     x = int(input())
     print(linear_search(l,x))
