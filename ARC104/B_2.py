import sys
sys.setrecursionlimit(10 ** 8)

N, S = map(str, sys.stdin.readline().strip().split())
N = int(N)

# 7 ATAGCTA
# 8 ATCGCGTA
# 6 CGACGT
# 4 AGTC


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
            continue

    if check(S[n - 1], S[n]):
        dp[n] = dp[n - 2] + 1
        continue

    if n < 3:
        continue
    count = 1
    while dp[n - count] != 0 and (n - 1 - count * 2 >= 0):
        count += 1
    count -= 1
    if count <= 0:
        if check(S[n], S[n - 2 * count - 1]):
            if n - 2 * count - 2 >= 0:
                dp[n] = dp[n - 2 * count - 2] + 1
            else:
                dp[n] = 1
            continue

    if count_a == count_c == count_g == count_t:
        dp[n] += 1
        if n == 3:
            continue

    s = S[n - 3: n + 1]
    if ('A' in s) and ('T' in s) and ('G' in s) and ('C' in s):
        if n > 4:
            dp[n] = dp[n - 4] + 1
        else:
            dp[n] = 1



print(sum(dp))
