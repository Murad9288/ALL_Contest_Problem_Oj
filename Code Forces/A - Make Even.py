for _ in range(int(input())):
    number = list(map(int,input()))
    n = []
    for i in number:
          n.append(1-(i%2))
    if(number[-1]%2 == 0):
          print(0)
    elif(sum(n) == 0):
          print(-1)
    elif(number[0]%2 == 0):
          print(1)
    else:
          print(2)
