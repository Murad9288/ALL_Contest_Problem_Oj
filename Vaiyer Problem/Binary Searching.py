# Def Function diye kora..
'''
def Binary_search(L,n):
     left, right = 0, len(L)-1
     while left <= right:
          middle = (left + right) // 2
          if L[middle] == n:
               print(middle + 1)
               break
          elif L[middle] < n:
               left = middle + 1
          else:
               right = middle - 1
     else:
          print("Sorry the number of binary search not value..!")

if __name__ == "__main__":
     while True:
          L = list(map(int,input().split()))
          n = int(input("Please enter your Binary search number: "))
          Binary_search(L,n)
'''
# Function baad diye...
'''
Li = list(map(int,input("input number obosshoy sorted dewa lagbe: ").split()))
n = int(input("Bainary Number searching input hote: "))
L, R = 0, len(Li) - 1 # eikhane L er man jodi 1 dewa hoy, tahole R er man 'len(Li)' dite hobe...r 0 thakle 'len(Li) -1' dite hobe..
while L <= R:
     M = (L+R) // 2
     if Li[M] == n:
          print(M + 1)
          break
     elif Li[M] < n:
          L = M + 1
     else:
          R = M - 1
else:
     print("Sorry the number is not binary search list")
'''
# ami nije korechi bujhar jonno...
'''
L = [1,2,3,4,5,6,7,8,9,10]
print("Main List: ",L)
N = int(input())
left, right = 0, len(L) - 1
print("Total Length: ",right)
while left <= right:
     mid = (left + right)//2
     if L[mid] == N:
          print("Baniry Position: ",mid + 1)
          break
     elif L[mid] < N:
          left = mid + 1
          print("left position : ",left)
     else:
          right = mid - 1
          print("right position: ",right)
else:
     print("Sorry wrong  number: ")
'''

