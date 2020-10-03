import sys
sys.setrecursionlimit(10 ** 8)

N, S = map(str, sys.stdin.readline().strip().split())
N = int(N)


def check(s1, s2):
    if s1 == 'A' and s2 == 'T':
        return True
    if s1 == 'T' and s2 == 'A':
        return True
    if s1 == 'C' and s2 == 'G':
        return True
    if s1 == 'G' and s2 == 'C':
        return True
    return False


dp = [0] * N
dp2 = [0] * N

s1 = S[0]
for n in range(N - 1):
    s2 = S[n + 1]

    if n == 0:
        if check(s1, s2):
            dp[1] = 1
        s1 = s2
        continue

    if check(s1, s2):
        dp[n + 1] = dp[n - 1] + 1
    s1 = s2




print(dp)
print(dp2)
print(sum(dp))
