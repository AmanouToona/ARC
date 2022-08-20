import sys
import itertools


def main():
    _ = int(input())
    A = list(map(int, sys.stdin.readline().strip().split()))

    A = sorted(A)
    A = list(reversed(A))
    A = A[:3]
    A = [str(a) for a in A]

    ans = 0
    for i in itertools.permutations(A):
        _ans = "".join(i)
        _ans = int(_ans)

        ans = max(ans, _ans)

    print(ans)
    return


if __name__ == "__main__":
    main()
