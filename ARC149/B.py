import sys

sys.setrecursionlimit(10 ** 8)


def main():
    N = int(input())

    A = list(map(int, sys.stdin.readline().strip().split()))
    B = list(map(int, sys.stdin.readline().strip().split()))

    ab = []
    for a, b in zip(A, B):
        ab.append((a, b))

    ab.sort(key=lambda x: x[0])

    dp = [float("inf")] * N
    for a, b in ab:
        if dp[0] > b:
            dp[0] = b
            continue

        ok = N
        ng = 0
        while ok - ng > 1:
            mid = (ok + ng) // 2
            if dp[mid] >= b:
                ok = mid
            else:
                ng = mid

        dp[ok] = b

    ok = 0
    ng = N
    while ng - ok > 1:
        mid = (ng + ok) // 2

        if dp[mid] == float("inf"):
            ng = mid
        else:
            ok = mid

    ans = N + ok + 1
    print(ans)

    return


if __name__ == "__main__":
    main()
