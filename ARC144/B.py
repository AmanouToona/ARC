import sys
import math


def main():
    N, a, b = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    A.sort()

    left = 0
    right = 3 * 10**14 + 1

    def judge(mid):
        rest_b = 0

        for aa in A:
            if aa < mid:
                rest_b += math.ceil((mid - aa) / a)
            else:
                rest_b -= math.floor((aa - mid) / b)

        return rest_b <= 0

    while right - left > 1:
        mid = (right + left) // 2

        if judge(mid):
            left = mid
        else:
            right = mid

    print(left)

    return


if __name__ == "__main__":
    main()
