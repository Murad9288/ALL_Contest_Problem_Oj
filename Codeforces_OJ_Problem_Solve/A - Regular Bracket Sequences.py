for _  in range(int(input())):
     n = int(input())
     for i in range(1,n+1):
          print("("*i, end= "")
          print(")"*i, end= "")

          temp = n-i
          for j in range(1,temp+1):
               print("(", end= "")
               print(")", end ="")

          print()
