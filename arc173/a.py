import sys

sys.setrecursionlimit(10**8)


def get_digit(n):
    res = 0
    while n > 0:
        res += 1
        n //= 10
    return res


def sep(n):
    res = []
    while n:
        res.append(n % 10)
        n //= 10
    res.reverse()
    return res


def count_eq(n):
    # dp[今の桁数][前の桁の数][is_noneq][超えていない?][all_zero]

    se = sep(n)

    digit = get_digit(n)
    dp = [[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(10)] for _ in range(digit + 1)]
    dp[0][0][0][0][1] = 1

    for dig in range(digit):
        for pre in range(10):
            for is_neq in range(2):
                for ove in range(2):
                    for zero in range(2):
                        for n in range(10):
                            # dp[今の桁数][前の桁の数][is_noneq][超えていない?][all_zero]
                            if n == 0 and zero:
                                dp[dig + 1][0][0][1][1] = 1
                                continue

                            if ove and n > se[dig]:
                                continue

                            now = dp[dig][pre][is_neq][ove][zero]

                            if pre == n:
                                if n < se[dig]:
                                    dp[dig + 1][n][1][1][0] += now
                                    continue
                                if n == se[dig]:
                                    dp[dig + 1][n][1][0][0] += now
                                    continue
                                dp[dig + 1][n][1][1][0] += now

                            if n < se[dig] or ove:
                                dp[dig + 1][n][is_neq][1][0] += now

                            if n == se[dig]:
                                dp[dig + 1][n][is_neq][0][0] += now

    res = 0
    for i in range(10):
        # print(dp[digit][i][1][1][0])
        res += dp[digit][i][1][1][0]

    return res


def solve(n):
    ng = 0
    ok = 10**10

    while ok - ng > 1:
        mid = (ok + ng) // 2

        n_eq = count_eq(mid)
        n_neq = mid - n_eq
        # print(f"{mid=}, {n_eq=}, {n_neq=}")

        if n_neq >= n:
            ok = mid
        else:
            ng = mid

    return ok


def main():
    T = int(input())

    # print(count_eq(T))

    # print(solve(T))

    for _ in range(T):
        case = int(input())
        ans = solve(case)
        print(ans)

    return


if __name__ == "__main__":
    main()
