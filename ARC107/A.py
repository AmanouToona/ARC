import sys

import sys

mod = 998244353
 
A, B, C = map(int, sys.stdin.readline().strip().split())

AA = A * (A + 1) // 2 % mod
BB = B * (B + 1) // 2 % mod
CC = C * (C + 1) // 2 % mod

ans = AA * BB * CC % mod

print(int(ans))
