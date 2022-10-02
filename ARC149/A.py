import sys

sys.setrecursionlimit(10 ** 8)


def can(X, rep):
    res = rep

    bit = 0

    s = set()
    while res:
        bit += 1

        res %= X
        if res == 0:
            return bit

        if res in s:
            break

        s.add(res)
        res *= 10
        res += rep

    return 0


def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    ans = -1
    for bit in range(1, 10):
        for y in range(N + 1):
            if ((10 ** y - 1) * bit) % (9 * M) == 0:
                K = ((10 ** y - 1) * bit) % (9 * M)
                ans = max(ans, K * M)

    print(ans)

    return


if __name__ == "__main__":
    main()
