import sys

sys.setrecursionlimit(10 ** 8)


def solve():
    N, K = map(int, sys.stdin.readline().strip().split())
    S = input().strip()

    cusum1 = [0] * (N + 1)
    cusumq = [0] * (N + 1)

    for i, s in enumerate(S):
        if s == "1":
            cusum1[i + 1] = 1
        elif s == "?":
            cusumq[i + 1] = 1

    for i in range(len(cusumq) - 1):
        cusum1[i + 1] += cusum1[i]
        cusumq[i + 1] += cusumq[i]

    cnt = 0
    for right in range(K, len(cusum1)):
        left = right - K

        # 1 にしたい領域が 連続する 1 にできるか？
        if K == (cusum1[right] - cusum1[left]) + (cusumq[right] - cusumq[left]):
            # 1 にする領域以外に 1 が含まれていないか？
            if cusum1[-1] - (cusum1[right] - cusum1[left]) == 0:
                cnt += 1

    if cnt == 1:
        print("Yes")
    else:
        print("No")
    return


def main():
    T = int(input())

    for _ in range(T):
        solve()
    return


if __name__ == "__main__":
    main()
