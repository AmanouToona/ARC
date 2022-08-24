import sys


def main():
    N, M, K = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))

    def judge(x):
        # x を作れるか?

        cost = [0] * N
        for i, a in enumerate(A):
            for bit in range(31, -1, -1):
                if cost[i] != 0:
                    continue
                if x & (1 << bit) == 0:
                    continue
                if a & (1 << bit):
                    continue

                cost[i] = x & ((1 << (bit + 1)) - 1) - a & (1 << ((bit + 1) - 1))

        cost.sort()
        return sum(cost[:K]) <= M

    ok = 0
    ng = 1 << 31
    while ng - ok > 1:
        mid = (ng + ok) // 2

        if judge(mid):
            ok = mid
        else:
            ng = mid

    print(ok)

    return


if __name__ == "__main__":
    main()
