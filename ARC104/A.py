import sys
sys.setrecursionlimit(10 ** 8)

A, B = map(int, sys.stdin.readline().strip().split())

X = int((A + B) / 2)
Y = int((A - B) / 2)

print(X, Y)
