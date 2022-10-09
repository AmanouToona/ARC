import sys
from itertools import groupby

sys.setrecursionlimit(10 ** 8)


def solve():
    _, K = map(int, sys.stdin.readline().strip().split())
    S = input().strip()

    rle = []
    grouped = groupby(S)
    for k, v in grouped:
        rle.append([k, int(len(list(v)))])

    # 1 の間にある ? は 1にしなければならない 0 の間にある ? は 0に
    for i in range(len(rle)):
        if i == 0 or i == len(rle) - 1:
            continue
        if rle[i][0] != "?":
            continue
        if rle[i - 1][0] == rle[i + 1][0]:
            rle[i][0] = rle[i - 1][0]

    # 同一番号は結合する
    _rle = []
    for i in range(len(rle)):
        if i == 0:
            _rle.append(rle[i])
            continue
        if _rle[-1][0] == rle[i][0]:
            _rle[-1][1] += rle[i][1]
            continue
        _rle.append(rle[i])

    rle = []
    for k, v in _rle:
        rle.append((k, v))

    # ここから ===========
    # 断絶された1があるか?
    cnt_one = 0
    for k, _ in rle:
        if k == "1":
            cnt_one += 1

    if cnt_one > 1:
        print("No")
        return

    if cnt_one == 0:
        can_cnt = 0
        for k, v in rle:
            if k == "0":
                continue
            if v < K:
                continue
            if v > K:
                print("No")
                return
            can_cnt += 1
        if can_cnt == 1:
            print("Yes")
        else:
            print("No")
            return

    use = []
    for i in range(len(rle)):
        if rle[i][0] == "1":
            if rle[i][1] > K:
                print("No")
                return

            if i > 0 and rle[i - 1][0] != "0":
                use.append(rle[i - 1])
            use.append(rle[i])
            if i + 1 < len(rle) and rle[i + 1][0] != "0":
                use.append(rle[i + 1])

    if len(use) <= 2:
        long = sum([v for _, v in use])
        if K <= long:
            print("Yes")
            return

    length = sum([v for _, v in use])
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
