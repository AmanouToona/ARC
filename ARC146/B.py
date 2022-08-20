import sys


def main():
    N, M, K = map(int, sys.stdin.readline().strip().split())
    A = list(map(int, sys.stdin.readline().strip().split()))
    A.sort()
    A = list(reversed(A))

    ans_bit = ["0"] * 31
    use = [False] * N

    for bit in range(31, -1, -1):
        want = 0
        count = 0
        for a in A[:K]:
            if count >= K:
                break
            if not use and a > 1 << bit:
                continue
            count += 1
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

    ans = "".join(list(reversed(ans_bit)))
    print(int(str(ans), 2))

    return


if __name__ == "__main__":
    main()
