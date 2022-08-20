import sys


def main():
    N, M, K = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))

    ans_bit = ["0"] * 31
    use = [False] * N

    for bit in range(30, -1, -1):
        want = 0

        if len(A) > K:
            A = sorted(A)
            A = list(reversed(A))
            t_A = [((1 << bit) - (a & ((1 << (bit + 1)) - 1)), a) for a in A]
            t_A = sorted(t_A, key=lambda x: x[0])
            A = [a for _, a in t_A]

        for a in A[:K]:
            if not use and a > 1 << bit:
                continue
            # print(f"a: {a}, bit: {bit}")
            # print(a & ((1 << (bit + 1)) - 1))
            # print((1 << bit) - (a & ((1 << (bit + 1)) - 1)))
            if a >> bit & 1:
                continue
            else:
                # print(a & ((1 << (bit + 1)) - 1))
                want += (1 << bit) - (a & ((1 << (bit + 1)) - 1))

        if want == 0:
            ans_bit[bit] = "1"
        elif want <= M:
            M -= want
            ans_bit[bit] = "1"

            for i in range(K):
                if A[i] >> bit & 1:
                    continue
                else:
                    A[i] += (1 << bit) - (A[i] & ((1 << (bit + 1)) - 1))
        if ans_bit[bit] == "1":
            A = A[:K]

    ans = "".join(list(reversed(ans_bit)))
    print(int(str(ans), 2))

    return


if __name__ == "__main__":
    main()
