import sys
sys.setrecursionlimit(10 ** 8)

N, S = map(str, sys.stdin.readline().strip().split())
N = int(N)

# 7 ATAGCTA
# 8 ATCGCGTA
# 6 CGACGT
# 4 AGTC
# 6 TCTGAA


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
dp2 = [float('inf')] * N  # 遠点の記録

count_a = 0
count_t = 0
count_g = 0
count_c = 0

for n in range(1, N):
    if S[n] == 'A':
        count_a += 1
    elif S[n] == 'T':
        count_t += 1
    elif S[n] == 'G':
        count_g += 1
    else:
        count_c += 1

    if n == 1:
        if check(S[n - 1], S[n]):
            dp[n] = 1
            dp2[n] = 0
            continue

    if check(S[n - 1], S[n]):
        dp[n] = dp[n - 2] + 1
        dp2[n] = dp2[n - 2]
        continue

    if dp2[n - 1] != float('inf') and (dp2[n - 1] > 0):
        m = int(dp2[n - 1] - 1)
        if check(S[m], S[n]):
            dp[n] = dp[m] + 1
            dp2[n] = m - 1

    if n < 3:
        continue

    s = S[n - 3: n + 1]
    if ('A' in s) and ('T' in s) and ('G' in s) and ('C' in s):
        dp[n] = dp[n - 4] + 1
        if n == 3:
            dp2[n] = 0
        else:
            dp2[n] = dp2[n - 4]

print(sum(dp))
