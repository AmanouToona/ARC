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

    # 1 の間にある ? は 1にしなければならない
    new_rle = []
    for i in range(len(rle)):
        if rle[i][0] != "?":
            new_rle.append(rle[i])
            continue

        if i > 0 and i + 1 < len(rle) and rle[i - 1][0] == "1" and rle[i + 1][0] == "1":
            new_rle.append(("1", rle[i][1]))
            continue
        new_rle.append(rle[i])

    _rle = []
    for i in range(len(new_rle)):
        if i == 0:
            _rle.append([new_rle[i][0], new_rle[i][1]])
            continue

        if new_rle[i][0] == new_rle[i - 1][0]:
            _rle[-1][1] += new_rle[i][1]
            continue

        _rle.append([new_rle[i][0], new_rle[i][1]])

    rle = []
    for k, v in _rle:
        rle.append((k, v))

    # ここから ===========
    # 0で断絶された1があるか?
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

    use = []
    for i in range(len(rle)):
        if rle[i][0] == "1":
            if i > 0 and rle[i - 1][0] == "?":
                use.append(rle[i - 1])
            use.append(rle[i])
            if i + 1 < len(rle) and rle[i + 1][0] == "?":
                use.append(rle[i + 1])

            break

    if len(use) <= 2:
        short = 0
        long = 0
        for k, v in use:
            if k == "1":
                short += v
                long += v
                continue
            long += v

        if K <= long and short <= K:
            print("Yes")
            return

    length = 0
    for k, v in use:
        length += v
    if length == K:
        print("Yes")
        return
    print("No")
    return


def main():
    T = int(input())

    for _ in range(T):
        solve()
    return


if __name__ == "__main__":
    main()
