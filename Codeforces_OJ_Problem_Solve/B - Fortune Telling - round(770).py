for _ in range(int(input())):
    n, a, g = map(int, input().split())
    arr = list(map(int, input().split()))
    a += sum(arr)
    if a % 2 == g % 2:
        print("Alice")
    else:
        print("Bob")
