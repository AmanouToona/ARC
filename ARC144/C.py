import sys


def main():
    N, K = map(int, sys.stdin.readline().strip().split())

    pos1 = N
    while pos1 > 0:
        right = N + 1 - pos1
        left = (right + 1) % N

        if abs(N - right) < K:
            pos1 -= 1
            continue
        if abs(left - 1) < K:
            pos1 -= 1
            continue
        break

    if pos1 == 0:
        print(-1)
        return

    ans = [0] * (N + 1)
    for i, p in enumerate(range(pos1, pos1 + N)):
        if p > N:
            p -= N
        ans[p] = i + 1

    pos = 0
    for i, an in enumerate(ans):
        i += 1
        if abs(pos1 - ans[i]) >= K and i - 1 >= K:
            pos = i
            break

    if pos != 0:
        left = pos
        right = pos1

        while right <= N:
            if (
                abs(ans[right] - left) >= K
                and abs(ans[left] - right)
                and ans[right] < ans[left]
            ):
                temp = ans[left]
                ans[left] = ans[right]
                ans[right] = temp
                right += 1
                left = 1

    ans = " ".join(ans[1:])
    print(ans)

    return


if __name__ == "__main__":
    main()
