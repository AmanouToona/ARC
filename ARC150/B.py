import sys
from math import ceil

sys.setrecursionlimit(10 ** 8)


def solve():
    A, B = map(int, sys.stdin.readline().strip().split())

    ans = float("inf")

    ans = min(ans, ceil(B / A) * A - B)



    print(ans)


def main():
    T = int(input())
    for _ in range(T):
        solve()
    return


if __name__ == "__main__":
    main()
