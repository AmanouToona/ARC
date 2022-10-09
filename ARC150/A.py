import sys
from itertools import groupby

sys.setrecursionlimit(10 ** 8)


def solve():
    N, K = map(int, sys.stdin.readline().strip().split())
    S = input().strip()

    rle = []
    grouped = groupby(S)
    for k, v in grouped:
        rle.append((k, int(len(list(v)))))

    # 連続させることができるか?
    one = False
    zero = False
    for k, _ in rle:
        if k == "?":
            continue
        if k == "1":
            if zero:
                print("No")
                return
            one = True
            continue
        if one:
            zero = True

    one = False
    short = 0
    stock = 0
    long = 0
    for k, v in rle:
        if k == "0" and not one:
            short = 0
            long = 0
            continue
        if k == "0" and one:
            break

        if k == "1":
            one = True
            long += v
            short += v + stock
            continue

        long += v
        if one:
            stock += v

    # print(f"s: {short}, l: {long}")
    # if K >= short and K <= long:
    #     print("Yes")
    # else:
    #     print("No")
    if long == K:
        print("Yes")
        return

    # 結合可能な q が 2つ以上あるならX
    q = False
    for k, v in rle:
        if k == "0":
            q = False
        if k == "?":
            if q:
                print("No")
                return
            q = True
            continue
    print("Yes")


def main():
    T = int(input())

    for _ in range(T):
        solve()
    return


if __name__ == "__main__":
    main()
