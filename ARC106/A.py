import sys
sys.setrecursionlimit(10 ** 8)

N = int(input())

A = 0
while True:
    A += 1
    B = 0
    while True:
        B += 1
        if 3 ** A + 5 ** B == N:
            print(A, B)
            sys.exit()

        if 3 ** A + 5 ** B > N:
            break

    if 3 ** A > N:
        break

print(-1)
