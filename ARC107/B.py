import sys

N, K = map(int, sys.stdin.readline().strip().split())


# x = a + b として考える
# y = c + d
x_max = min(2 * N, 2 * N + K)
x_min = max(2 + K, 2)

# print(f'x_max: {x_max}, x_min: {x_min}')

ans = 0
for x in range(x_min, x_max + 1):
    y = x - K
    cd = min(N, y - 1) - max(y - N, 1) + 1

    ab = min(N, x - 1) - max(x - N, 1) + 1
    # print(f'ab: {ab}')

    pls = cd * ab

    ans += pls

    # print(f'x: {x} pls:{pls}')

print(ans)

