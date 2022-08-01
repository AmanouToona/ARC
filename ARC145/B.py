import sys


def main():
    N, A, B = map(int, sys.stdin.readline().strip().split())

    if A <= B:
        win = max(0, N - (A - 1))
        print(win)
        return

    if N < A:
        print(0)
        return

    win = 0
    win += (N - B) // A * B

    k = N // A
    if k * A + B > N:
        win += N - k * A + 1

    print(win)

    return


if __name__ == "__main__":
    main()
