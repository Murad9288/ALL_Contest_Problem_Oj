A,B,C = map(float,input().split())
if A >=B+C:
    print("NAO FORMA TRIANGULO")
elif A^2 == B^2 + C^2:
    print("TRIANGULO RETANGULO")
elif A^2 > B^2 + C^2:
    print("TRIANGULO OBTUSANGULO")
elif A^2 < B^2 + C^2:
    print("TRIANGULO ACUTANGULO")
else:
    print("wrong")
