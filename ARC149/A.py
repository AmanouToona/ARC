import sys

sys.setrecursionlimit(10 ** 8)


def main():
    N, M = map(int, sys.stdin.readline().strip().split())

    answers = []
    for num in range(1, 10):
        res = 0
        for bit in range(1, N + 1):
            res *= 10
            res += num

            res %= M
            if res == 0:
                answers.append((num, bit))

    answers.sort(key=lambda x: -x[0])
    answers.sort(key=lambda x: -x[1])

    if not answers:
        print(-1)
    else:
        answer = answers[0]
        for _ in range(answer[1]):
            print(answer[0], end="")
        print()

    return


if __name__ == "__main__":
    main()
