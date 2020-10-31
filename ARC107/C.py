import sys

mod = 998244353

N, K = map(int, sys.stdin.readline().strip().split())
A = []
for n in range(N):
    A.append(list(map(int, sys.stdin.readline().strip().split())))

col_dic = [[j, i] for i, j in enumerate(A[0])]
col_dic.sort(key=lambda x: x[0])

col = [j for i, j in col_dic]



